#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-04-29
Purpose: substitution cipher
"""

import argparse
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='substitution cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='SEED',
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
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return char.upper() if random.choice([0, 1]) else char.lower()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    random.seed(args.seed)

    # Create a list of all the letters in the alphabet
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # Shuffle the alphabet using a random seed
    shuffled_alphabet = random.sample(alphabet, len(alphabet))

    # Create a dictionary map each letter to shuffled letter
    shuffled_dict = dict(zip(alphabet, shuffled_alphabet))
    if args.decode:  # if decode, switch the sequence
        shuffled_dict = dict(zip(shuffled_alphabet, alphabet))

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
                output_string += shuffled_dict.get(char.upper())
            else:
                output_string += char
        args.outfile.write(f'{output_string}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
