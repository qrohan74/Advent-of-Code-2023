import argparse
import importlib

from aoc2023.common.logger import Logger

###################
# Options
###################
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', action='store', dest='day', type=int, default=-1,
                    help='Run test day', required=True)
parser.add_argument('-p', '--part', action='store', dest='part', type=int, default=-1,
                    help='Run a specific part', required=True)
parser.add_argument('-z', '--puzzle', action='store', dest='puzzle', type=str, default=None,
                    help='Puzzle file')
parser.add_argument('-v', '--verbosity', action='count', dest='verbose', default=0,
                    help='Verbosity level')
args = parser.parse_args()

###################
# Configure
###################
Logger.set_level(args.verbose if args.verbose > 0 else Logger.INFO)

###################
# Run
###################
Logger.info('AOC 2023 - day %d, part %d' % (args.day, args.part))
Puzzle = getattr(importlib.import_module("aoc2023.day%d.part%d" % (args.day, args.part)), 'Puzzle')
puzzle = Puzzle()
puzzle.run()
