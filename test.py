#!/usr/bin/python3

import sys

input_file = sys.argv[1]

with open(input_file, 'r') as filereader:
    for row in filereader:
        print(f'Line is {row}')
        
        
