"""
Test script for batch processing 
"""

import sys
processing = __import__('1-batch_processing')

try:
    processing.batch_processing(10)
except BrokenPipeError:
    sys.stderr.close()