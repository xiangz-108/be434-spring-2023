#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-04-19
Purpose: Python grep
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

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
    file_num = len(args.files)
    pattern = re.compile(args.pattern, re.I if args.insensitive else 0)
    for files_index in args.files:
        for lines in filter(pattern.search, files_index):
            if file_num > 1:
                string1 = f'{files_index.name}:'
            else:
                string1 = ''
            args.outfile.write(f'{string1}{lines}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
