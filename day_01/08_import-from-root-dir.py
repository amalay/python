
# -----------------------------------------------------------------
# Import from parent directory using os.path.dirname method (Syntax: from {file} import {class})
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

# Add parent directory to system path.
sys.path.insert(0, parent_dir)  # sys.path.insert(0, parent_dir) OR sys.path.append(parent_dir)

# Print all paths exist in sys.path
# for item in sys.path:
#     print(item)
# print("\n-----------------------------------------------------------------")

# Importing constant file from root directory.
from constant import Messages, Maths

print(Messages.MESSAGE)     # Prints: Constant file is in root directory!
print(Messages.SEPERATOR)