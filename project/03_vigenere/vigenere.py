#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-04-29
Purpose: vigenere cipher
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--keyword',
                        help='A random seed',
                        metavar='KEYWORD',
                        default='CIPHER')

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
def encode(input_char, cipher_char):
    """encode via summation of index of input_char and cipher_char"""
    idx1 = ord(input_char) - 97
    idx2 = ord(cipher_char) - 97
    sum_idx = (idx1 + idx2) % 26
    result_char = chr(sum_idx + 97)
    return result_char


# --------------------------------------------------
def decode(input_char, cipher_char):
    """decode via index of input_char - index of cipher_char"""
    idx1 = ord(input_char) - 97
    idx2 = ord(cipher_char) - 97
    sum_idx = (idx1 - idx2) % 26
    result_char = chr(sum_idx + 97)
    return result_char


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    cipher = args.keyword

    # check each line, and change each character
    fh = args.file_input
    Lines = fh.readlines()
    ln_num = 0
    for ln in Lines:
        ln_num += 1
        output_string = ''
        char_index = 0
        for char in ln:
            if char.isalpha():
                code_ch = encode(char.lower(),
                                 cipher[char_index % len(cipher)].lower())
                if args.decode:
                    code_ch = decode(char.lower(),
                                     cipher[char_index % len(cipher)].lower())
                output_string += code_ch.upper()
                char_index += 1
            else:
                output_string += char

        args.outfile.write(f'{output_string}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
