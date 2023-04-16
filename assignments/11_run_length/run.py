#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-04-15
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()
    if os.path.isfile(args.str):
        with open(args.str, "rt", encoding='utf-8') as file:
            args.str = file.read().rstrip()
    return args


def rle(seq):
    """ Create RLE """

    compr = []
    count = 1
    char = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == char:
            count = count + 1
        else:
            compr.append([char, count])
            char = seq[i]
            count = 1
    compr.append([char, count])
    return compr


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.str
    list_seq = rle(seq)
    list_size = len(list_seq)
    compressed_seq = ''
    for i in range(0, list_size):
        for j in list_seq[i]:
            compressed_seq += str(j)
    string = compressed_seq.replace("1", "")
    print(string, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
