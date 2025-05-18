#!/usr/bin/python3
"""
Test script for user streaming (Task 1)
"""

from itertools import islice
from 0_stream_users import stream_users

def main():
    # Print first 6 users as shown in example
    for user in islice(stream_users(), 6):
        print(user)

if __name__ == "__main__":
    main()