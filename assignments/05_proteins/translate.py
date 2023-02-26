#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-02-26
Purpose: Translates a given DNA/RNA sequence to amino acids
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translates a given DNA/RNA sequence to amino acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_t = {}
    outfile_name = args.outfile
    seqs = args.sequence.upper()

    for line in args.codons:
        codon, proteins = line.split()
        codon_t[codon] = proteins

    for codon in [seqs[i:i + 3] for i in range(0, len(seqs), 3)]:
        outfile_name.write(codon_t.get(codon.upper(), '-'))

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
