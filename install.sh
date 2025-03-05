#!/bin/bash

set -e

echo "Installing Vacuum tool..."

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "Error: pip is not installed. Please install Python and pip first."
    exit 1
fi

# Install the vacuum package
pip install vacuum

echo "Vacuum has been successfully installed!"
echo "Run 'vacuum' followed by a GitHub repository URL to start using it."