#!/usr/bin/env python

import argparse
import helloworld


def parse_command_line():
    " parses args for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add short args
    parser.add_argument(
        "-bm", "--bestmusic",
        help="optional input of music type to test",
        type=str)

    # add long args
    parser.add_argument(
        "--crabtime",
        help="print days since the Crab Nebula Supernova Event, SN 1054",
        action="store_true")

    parser.add_argument(
        "--polite",
        help="print an eloquent and polite exit message",
        action="store_true")

    # parse args
    args = parser.parse_args()
    return args


def main():
    " run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        bestmusic=args.bestmusic,
        crabtime=args.crabtime,
        polite=args.polite)