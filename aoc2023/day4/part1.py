import re
import math
from operator import itemgetter
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
        super().__init__(4, 1, self.go)

    def go(self):
        """
        Run puzzle
        """
        s = 0
        for line in self.lines:
            line_card, line_values = [s.strip() for s in itemgetter(0, 1)(line.split(':'))]
            line_winning, line_draw = [s.strip() for s in itemgetter(0, 1)(line_values.split('|'))]
            common_numbers = list(set([int(n) for n in re.findall(r'\d+', line_winning)]).intersection(
                [int(n) for n in re.findall(r'\d+', line_draw)]))
            card_score = 0 if len(common_numbers) == 0 else math.pow(2, len(common_numbers) - 1)
            Logger.debug("%s: score=%d" % (line_card, card_score))
            s = s + card_score
        Logger.info("Result=%d" % s)
