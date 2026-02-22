#!/bin/bash
set -e

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
cd "$SCRIPT_DIR"

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run the whale alert Python script
echo "Starting ETH whale alert monitor..."
python3 whale_alert.py

