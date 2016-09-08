#!/usr/bin/env python
"""
Generates a random SAT instance.
"""
from __future__ import division
from __future__ import print_function

from sys import stdin
from sys import stderr

import random
import argparse

from satinstance import SATInstance
from solvers.watchlist import setup_watchlist
from solvers import recursive_sat
from solvers import iterative_sat

__author__ = 'David Evans'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("nvars", help="number of variables",
                        type=int)
    parser.add_argument("nclauses", help="number of clauses",
                        type=int)
    args = parser.parse_args()
    nvars = args.nvars
    nclauses = args.nclauses

    vars = set()
    for i in range(1, nvars + 1):
        vars.add('x' + str(i))

    fvars = frozenset(vars)
    clauses = set()
    # just print to stdout
    while len(clauses) < nclauses:
        vars = list(fvars)
        svars = []
        for lit in range(3):
            var = random.choice(vars) 
            vars.remove(var)
            svars.append(var)
        svars.sort()
        for index in range(len(svars)):
            if random.random() < 0.5:
                svars[index] = '~' + svars[index]

        clause = ' '.join(svars)
        if clause in clauses:
            print ("Found duplicate clause: " + clause)
        else:
            clauses.add(clause)

    for clause in clauses:
        print (clause)

if __name__ == '__main__':
    main()
