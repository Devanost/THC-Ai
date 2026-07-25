import json
from openai import OpenAI
from thc_ai.config import Config
from thc_ai.tools import TOOLS, TOOL_SCHEMAS

class Agent:
    def __init__(self, ui, memory, skills_manager):
        self.ui = ui
        self.memory = memory
        self.skills_manager = skills_manager
        self.client = OpenAI(api_key=Config.API_KEY, base_url=Config.API_BASE_URL)
        self.system_prompt = f"You are {Config.PROJECT_NAME}, an advanced agentic terminal assistant. Use tools to help the user."

    def run(self, user_input):
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Inject skills context
        relevant_skills = self.skills_manager.get_relevant_skills(user_input)
        if relevant_skills:
            skills_context = "\n\nAvailable Skills:\n" + "\n".join(relevant_skills)
            messages[0]["content"] += skills_context

        # Load history
        history = self.memory.get_history()
        messages.extend(history)
        messages.append({"role": "user", "content": user_input})
        
        # Save user message
        self.memory.save_message("user", user_input)

        while True:
            try:
                response = self.client.chat.completions.create(
                    model=Config.MODEL,
                    messages=messages,
                    tools=TOOL_SCHEMAS,
                    tool_choice="auto",
                    stream=True
                )

                full_content = ""
                tool_calls = []
                
                # Stream content and collect tool calls
                def content_generator():
                    nonlocal full_content
                    for chunk in response:
                        delta = chunk.choices[0].delta
                        if delta.content:
                            full_content += delta.content
                            yield delta.content
                        if delta.tool_calls:
                            for tc in delta.tool_calls:
                                if len(tool_calls) <= tc.index:
                                    tool_calls.append({
                                        "id": tc.id,
                                        "name": tc.function.name,
                                        "arguments": tc.function.arguments or ""
                                    })
                                else:
                                    if tc.function.arguments:
                                        tool_calls[tc.index]["arguments"] += tc.function.arguments

                ai_text = self.ui.stream_ai_response(content_generator())
                
                if ai_text:
                    messages.append({"role": "assistant", "content": ai_text})
                    self.memory.save_message("assistant", ai_text)

                if not tool_calls:
                    break

                # Handle tool calls
                messages.append({"role": "assistant", "tool_calls": [
                    {
                        "id": tc["id"],
                        "type": "function",
                        "function": {"name": tc["name"], "arguments": tc["arguments"]}
                    } for tc in tool_calls
                ]})

                for tc in tool_calls:
                    tool_name = tc["name"]
                    tool_args = json.loads(tc["arguments"])
                    self.ui.display_tool_call(tool_name, tool_args)
                    
                    tool_func = TOOLS.get(tool_name)
                    if tool_func:
                        output = tool_func(**tool_args)
                        self.ui.display_tool_output(output)
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tc["id"],
                            "name": tool_name,
                            "content": str(output)
                        })
                    else:
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tc["id"],
                            "name": tool_name,
                            "content": f"Error: Tool {tool_name} not found."
                        })

            except Exception as e:
                self.ui.display_error(str(e))
                break
