# -*- coding: utf-8 -*-

import argparse

parse = argparse.ArgumentParser()
parse.add_argument("haha", help="echo the string you use here", type=int)
args = parse.parse_args()
print args.haha**3
