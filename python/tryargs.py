#!/usr/bin/env python3

import os
import sys

file = sys.argv[1]
output = file.split('.')[0]

os.system(f"g++ -std=c++11 -O2 -Wall {file} -o {output}")
