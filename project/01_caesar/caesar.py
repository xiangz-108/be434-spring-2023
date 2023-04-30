#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-04-29
Purpose: caesar shift
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        default=False,
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('file_input',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    # specify the number of positions to shift the letters by
    shift = args.number
    if args.decode:
        shift = -shift

    # create a dictionary to map each letter to its shifted counterpart
    lookup_table = {}
    for i in range(26):
        # compute the shifted index for the current letter
        shifted_index = (i + shift) % 26
        # convert the index back to a letter using the ASCII code
        lookup_table[chr(i + 97)] = chr(shifted_index + 97)

    # check each line, and change each character
    fh = args.file_input
    Lines = fh.readlines()
    ln_num = 0
    for ln in Lines:
        ln_num += 1
        output_string = ''
        for char in ln:
            if char.isalpha():
                # use the dictionary to convert the letter
                output_string += lookup_table[char.lower()].upper()
            else:
                output_string += char
        args.outfile.write(f'{output_string}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
