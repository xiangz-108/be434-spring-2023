#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-02-10
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('songkey',
                        help='Solfege',
                        metavar='str',
                        type=str,
                        nargs='+',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    key_list = args.songkey
    music = {'Do': 'Do, A deer, a female deer',
             'Re': 'Re, A drop of golden sun',
             'Mi': 'Mi, A name I call myself',
             'Fa': 'Fa, A long long way to run',
             'Sol': 'Sol, A needle pulling thread',
             'La': 'La, A note to follow sol',
             'Ti': 'Ti, A drink with jam and bread'}
    for key in key_list:
        if key in music:
            print(f'{music.get(key)}')
        else:
            print(f'I don\'t know "{key}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
