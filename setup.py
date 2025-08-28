#!/usr/bin/env python3
"""
Setup script for Empathetic Code Reviewer - Mission 1 Solution
Automated installation and configuration helper
"""

import subprocess
import sys
import os
import json

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def check_api_key():
    """Check if OpenAI API key is configured"""
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print("✅ OpenAI API key found in environment")
        return True
    else:
        print("⚠️  OpenAI API key not found")
        print("Please set your API key:")
        print("  export OPENAI_API_KEY='your-api-key-here'")
        print("Get one from: https://platform.openai.com/api-keys")
        return False

def run_demo():
    """Run the demo version"""
    print("🚀 Running demo version...")
    try:
        subprocess.run([sys.executable, "demo_empathetic_reviewer.py"])
    except FileNotFoundError:
        print("❌ Demo file not found")

def create_sample_input():
    """Create a simple sample input file for testing"""
    sample = {
        "code_snippet": "def calc(x, y):\n    return x + y",
        "review_comments": [
            "Function name is too short",
            "Missing docstring", 
            "No type hints"
        ]
    }

    with open('test_input.json', 'w') as f:
        json.dump(sample, f, indent=2)

    print("📝 Created test_input.json for testing")

def main():
    """Main setup process"""
    print("💝 Empathetic Code Reviewer - Setup Assistant")
    print("="*55)

    # Install requirements
    if not install_requirements():
        return

    # Check API key
    has_api_key = check_api_key()

    # Create sample input
    create_sample_input()

    print("\n" + "="*55)
    print("🎯 Setup Complete!")
    print("="*55)

    if has_api_key:
        print("✅ Ready for full empathetic analysis:")
        print('  python empathetic_code_reviewer.py test_input.json')
    else:
        print("⚠️  Demo mode available (no API key required):")
        print("  python demo_empathetic_reviewer.py")

    print("\n📚 Files included:")
    print("  - empathetic_code_reviewer.py (main solution)")
    print("  - demo_empathetic_reviewer.py (demo version)")
    print("  - sample_input_*.json (example inputs)")
    print("  - config.py (customization settings)")
    print("  - README.md (comprehensive documentation)")

    # Offer to run demo
    if not has_api_key:
        response = input("\n🤔 Would you like to run the demo now? (y/n): ")
        if response.lower() in ['y', 'yes']:
            run_demo()

if __name__ == "__main__":
    main()
