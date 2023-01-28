#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-01-28
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greetings and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='A name to greeting',
                        metavar='str',
                        type=str,
                        default='Stranger')
                        

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    gre= args.greeting
    nam= args.name
    ex=args.excited
    sym='.' if ex==False else '!'

    print(f'{gre}, {nam}{sym}')



# --------------------------------------------------
if __name__ == '__main__':
    main()
