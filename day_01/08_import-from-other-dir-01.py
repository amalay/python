
# -----------------------------------------------------------------
# Import from other directory (Syntax: from {directory} import {file})
# -----------------------------------------------------------------
import sys

# Setting path to parent directory.
sys.path.append('..')   # .. denote the parent directory.

# Importing constant from day_02 directory.
from day_02 import constant

print(constant.MESSAGE)     # Prints: Constant file is in another directory (day_02)!