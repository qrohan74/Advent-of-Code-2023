import re

from aoc2023.common.logger import Logger
from aoc2023.common.puzzle import DailyPuzzle


class Puzzle(DailyPuzzle):
    """
    A puzzle class
    """
    def __init__(self):
        """
        Puzzle creation
        """
        super().__init__(1, 1, self.go)  # Day 1

    def go(self):
        """
        Run puzzle
        """
        s = 0
        for line in self.lines:
            line_without_char = re.sub(r"\D", '', line)
            s = s + (int(line_without_char[0]) * 10 + int(line_without_char[-1]))
        Logger.info("Result=%d" % s)
