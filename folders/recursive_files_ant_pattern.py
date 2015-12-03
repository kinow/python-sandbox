#!/usr/bin/env python3

import glob

"""Recursively executes an action expanding using a glob."""

def main():
    for filename in glob.glob("*/*/*.EDT"):
        print("Executing a script or command with file %s" % filename)

if __name__ == '__main__':
    main()
