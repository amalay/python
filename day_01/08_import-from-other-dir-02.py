
# -----------------------------------------------------------------
# Import from other directory using os.path.abspath() OR os.path.realpath() method
# -----------------------------------------------------------------
import sys
import os

# Getting the current file path.
current_file_path = os.path.realpath(__file__)  # os.path.realpath(__file__) OR os.path.abspath(__file__)
print('Current file path: ', current_file_path)
print("\n-----------------------------------------------------------------")

# Getting current directory.
current_dir = os.path.dirname(current_file_path)
print('Current directory: ', current_dir)
print("\n-----------------------------------------------------------------")

# Getting parent directory.
parent_dir = os.path.dirname(current_dir)
print('Parent directory: ', parent_dir)
print("\n-----------------------------------------------------------------")

# Append parent directory to system path.
sys.path.append(parent_dir)

# Importing constant from day_02 directory.
from day_02 import constant

print(constant.MESSAGE)     # Prints: Constant file is in another directory (day_02)!
print(constant.SEPERATOR)