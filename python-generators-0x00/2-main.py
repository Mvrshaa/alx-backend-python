#!/usr/bin/python3
"""
Test script for lazy pagination (Task 3)
"""

import sys
from 2_lazy_paginate import lazy_paginate

def main():
    try:
        # Test pagination with 100 items per page
        for page in lazy_paginate(100):
            for user in page:
                print(user)
                print()  # Empty line between users
                
    except BrokenPipeError:
        sys.stderr.close()

if __name__ == "__main__":
    main()