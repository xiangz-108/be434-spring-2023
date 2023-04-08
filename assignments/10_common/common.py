#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-04-08
Purpose: Find Common Words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))
    parser.add_argument('FILE2',
                        metavar='FILE1',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1_set = set(args.FILE1.read().split())
    file2_set = set(args.FILE2.read().split())
    common_set = file1_set.intersection(file2_set)
    for word in common_set:
        if len(common_set) != 0:
            print(word, file=args.outfile)
        else:
            print(" No common words!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
