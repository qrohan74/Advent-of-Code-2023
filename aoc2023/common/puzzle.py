import os
from aoc2023.common.logger import Logger


def _todo():
    print("TODO")


class DailyPuzzle:
    """
    A class for running puzzle
    """
    def __init__(self, day, part, callback=_todo):
        """
        Puzzle creation
        """
        self.day = day
        self.part = part
        self.callback = callback
        self.lines = None

    def run(self, puzzle=None):
        """
        Run the puzzle
        """
        if puzzle is None:
            # puzzle not specified, use the default one
            fpath = os.path.join(os.getcwd(), "aoc2023", "day%s" % self.day, "puzzle%s.txt" % self.part)
            assert os.path.isfile(fpath), ("%s is not a file" % fpath)
            puzzle = os.path.abspath(fpath)
            Logger.spam("Use default puzzle: %s" % fpath)

        # read puzzle
        with open(puzzle, 'r') as file:
            self.lines = [line.rstrip() for line in file]

        # run
        self.callback()
