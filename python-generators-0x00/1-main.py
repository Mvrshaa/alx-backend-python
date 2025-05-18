#!/usr/bin/python3
"""
Test script for batch processing (Task 2)
"""

import sys
from 1_batch_processing import batch_processing

def main():
    try:
        # Process in batches of 50 as per example
        for user in batch_processing(50):
            print(user)
            print()  # Empty line between users
            
    except BrokenPipeError:
        # Handle pipe errors gracefully
        sys.stderr.close()

if __name__ == "__main__":
    main()