#!/usr/bin/env python

import pybel

import argparse

def main():
    argp = argparse.ArgumentParser(
        prog = 'Pybel',
        description = 'Fetches books from the Library of Babel (https://libraryofbabel.info/)')

    argp.add_argument('hexagon')
    argp.add_argument('wall', type=int)
    argp.add_argument('shelf', type=int)
    argp.add_argument('volume', type=int)

    args = argp.parse_args()

    print(pybel.getbook(args.hexagon, args.wall, args.shelf, args.volume))

if __name__ == "__main__":
    main()

