#!/usr/bin/python3
"""
Test script for age calculation (Task 4)
"""

from 4_stream_ages import calculate_average_age

def main():
    average = calculate_average_age()
    print(f"Average age of users: {average:.2f}")

if __name__ == "__main__":
    main()