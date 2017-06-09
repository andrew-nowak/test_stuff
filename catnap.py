#!/usr/bin/env python2

import argparse
import os
import time
import sys

def cat_stdin():
    for line in sys.stdin:
        sys.stdout.write(line)


def main(args):
    for filename in args.file:
        if filename != '-' and not os.path.isfile(filename):
            raise Exception("{}: no such file".format(filename))

    time.sleep(args.time)
    if args.file.count('-') > 1:
        raise Exception("stdin explicitly mentioned more than once")
    if len(args.file) == 0:
        cat_stdin()
    else:
        for filename in args.file:
            if filename != '-':
                with open(filename, 'r') as f:
                    for line in f:
                        sys.stdout.write(line)

            else:
                cat_stdin()


if __name__ == "__main__":
    desc = "Sleeps for a few seconds, then concatenates FILE(s)"\
           "to standard output.\n\n"\
           "With no FILE, or when FILE is -, read standard input."

    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument("file", action="store",
                        default=['-'], nargs='*')
    parser.add_argument("--time", dest="time", action="store",
                        default=5, type=int, nargs='?',
                        help="How long to sleep in seconds")
    args = parser.parse_args()
    main(args)
