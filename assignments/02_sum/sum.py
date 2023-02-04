#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-02-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nums',
                        help='Numbers to add',
                        metavar='INT',
                        nargs='+',
                        type=int)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_list = args.nums
    list_string = map(str, num_list)
    num_sum = sum(num_list)
    eqn_left = ' + '.join(list_string)
    print(f'{eqn_left} = {num_sum}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
