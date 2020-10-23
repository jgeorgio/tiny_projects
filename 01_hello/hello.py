#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--name', default='World', help='Name to greet')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, ' + args.name + '!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
