#!/bin/bash

# THC Ai - One-liner Installer
set -e

echo "🚀 Installing THC Ai..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install it first."
    exit 1
fi

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Clone the repository (silent)
echo "📦 Fetching latest version from GitHub..."
git clone --quiet https://github.com/Devanost/THC-Ai.git .

# Install the package
echo "⚙️ Installing dependencies and setting up 'thc-ai' command..."
pip3 install . --quiet

# Clean up
cd ~
rm -rf "$TEMP_DIR"

echo "✅ THC Ai installed successfully!"
echo "👉 Type 'thc-ai' to start talking."
