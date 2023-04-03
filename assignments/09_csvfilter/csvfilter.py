#!/usr/bin/env python3
"""
Author : xiangzhang <xiangzhang@localhost>
Date   : 2023-03-28
Purpose: Filter delimited records
"""

import argparse
import csv
import re
import sys
# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        metavar='val',
                        help='Value for filter',
                        type=str,
                        default=None,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        metavar='col',
                        help='Column for filter',
                        type=str,
                        default="")

    parser.add_argument('-o',
                        '--outfile',
                        metavar='OUTFILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default="out.csv")

    parser.add_argument('-d',
                        '--delimiter',
                        metavar='delim',
                        help='Input delimiter',
                        type=str,
                        default=",")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    count = 0
    for rec in reader:
        if args.col != "":
            if args.col not in rec:
                err_string1 = f'--col "{args.col}" not a valid column! \n'
                err_string2 = 'Choose from '
                for key, value in rec.items():
                    err_string2 += key + ', '
                sys.stderr.write(err_string1+err_string2[:-2]+'\n')
                sys.exit(1)
                break

        for key, value in rec.items():
            if re.search(args.val, value, re.IGNORECASE):
                if args.col == "":
                    writer.writerow(rec)
                    count += 1
                    break
                if args.col.upper() == key.upper():
                    writer.writerow(rec)
                    count += 1
                    break

    output_string = f'Done, wrote {count} to "{args.outfile.name}".'
    print(output_string)


# --------------------------------------------------
if __name__ == '__main__':
    main()
