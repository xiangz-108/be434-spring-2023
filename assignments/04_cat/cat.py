#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-02-19
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='A positional argument',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        default=False,
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh_list = args.FILE
    int_arg = args.number

    for fh in fh_list:
        Lines = fh.readlines()
        ln_num = 0
        for ln in Lines:
            ln_num += 1
            if int_arg:
                ln = "     "+str(ln_num)+'\t'+ln
            print(f'{ln}', end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
