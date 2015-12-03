#!/usr/bin/env python3

import os
import argparse

from random import sample
from random import randint
from shutil import copyfile

"""Creates a directory structure consisting of year/month/files. Where year
is a number between 1980 and 2014; month is a number between 1 (january) and
12 (december); and files is a number n of files. Where n can be any integer
between 0 and 100."""

DEFAULT_MIN_YEAR = 1980
DEFAULT_MAX_YEAR = 2014
DEFAULT_MIN_MONTH = 1
DEFAULT_MAX_MONTH = 12
DEFAULT_NUMBER_SAMPLE_FILES = 10

def generate_random_samples(from_arg, to_arg, amount):
    return sample(xrange(from_arg, to_arg+1), amount)

def create_year_directories(base_dir, years, months, sample_file):
    for year in generate_random_samples(DEFAULT_MIN_YEAR, DEFAULT_MAX_YEAR, years):
        directory = os.path.join(base_dir, str(year))
        if not os.path.exists(directory):
            print("Creating directory for year %s" % directory)
            os.makedirs(directory)
        create_month_directories(base_dir, year, months, sample_file)

def create_month_directories(base_dir, year ,months, sample_file):
    for month in generate_random_samples(DEFAULT_MIN_MONTH, DEFAULT_MAX_MONTH, months):
        directory = os.path.join(base_dir, str(year), str(month))
        if not os.path.exists(directory):
            print("Creating directory for month %s" % directory)
            os.makedirs(directory)
            copy_sample_file(directory, sample_file)

def copy_sample_file(directory, sample_file):
    for x in xrange(0, DEFAULT_NUMBER_SAMPLE_FILES + 1):
        destination_file = os.path.join(directory, os.path.basename(sample_file) + '_' + str(x))
        print("Copying sample file to %s" % destination_file)
        copyfile(sample_file, destination_file)

def main(base_dir, years, months, sample_file):
    create_year_directories(base_dir, years, months, sample_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates a folder hierarchy with years, months and a sample file.')
    parser.add_argument('base_dir', metavar='base_dir', type=str, help='base directory to create folders')
    parser.add_argument('years', metavar='years', type=int, help='number of years')
    parser.add_argument('months', metavar='months', type=int, help='number of months')
    parser.add_argument('sample_file', metavar='sample_file', type=str, help='file to be copied as file_$idx')

    args = parser.parse_args()
    main(args.base_dir, args.years, args.months, args.sample_file)
