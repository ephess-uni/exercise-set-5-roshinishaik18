""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
import argparse
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    obj_parse = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile")
    obj_parse.add_argument("infile", type=argparse.FileType('r'))
    obj_parse.add_argument("outfile", type=argparse.FileType('w'))
    args_p = obj_parse.parse_args()
    data = np.loadtxt("input_data.txt")
    mean_val = np.mean(data)
    mean_val1 = data - mean_val
    std_data = np.std(mean_val1)
    processed = mean_val1 / std_data
    np.savetxt(obj_parse.outfile, processed,fmt='%.2e')
