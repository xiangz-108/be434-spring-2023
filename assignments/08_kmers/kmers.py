#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-03-21
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))
    parser.add_argument('file2',
                        metavar='FILE1',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()
    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')
    return args


def count_kmers(file, kmer):
    """ Count and put kmers to words_count """
    words1 = {}
    for line in file:
        for word in line.split():
            for kmer_pick in find_kmers(word, kmer):
                if kmer_pick not in words1:
                    words1[kmer_pick] = 1
                else:
                    words1[kmer_pick] += 1
    return words1


def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


def main():
    """Make a jazz noise here"""
    args = get_args()
    f1 = args.file1.read().split()
    f2 = args.file2.read().split()
    w_f1 = count_kmers(f1, args.kmer)
    w_f2 = count_kmers(f2, args.kmer)
    common = set(w_f1).intersection(set(w_f2))
    for word in common:
        if len(common) != 0:
            print(f'{word:10} {w_f1.get(word):5} {w_f2.get(word):5}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
