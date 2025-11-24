#!/usr/bin/env python
"""
K-Blacklist Entry Point
Wrapper to run the application from project root.
"""

import sys
import os

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

# Import and run main
from main import main

if __name__ == "__main__":
    main()
