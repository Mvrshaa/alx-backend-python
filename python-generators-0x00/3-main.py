"""
Test script for age calculation(stream ages) 
"""

import sys
stream_ages = __import__('4-stream_ages')

try:
    stream_ages.calculate_average_age()
except BrokenPipeError:
    sys.stderr.close()