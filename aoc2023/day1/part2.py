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
        super().__init__(1, 2, self.go)

    def go(self):
        """
        Run puzzle
        """
        s = 0
        pattern = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                   "nine": 9, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        for line in self.lines:
            li = 999
            lk = ''
            ri = -1
            rk = ''
            for k in pattern.keys():
                idx = line.find(k)
                if 0 <= idx < li:
                    li = idx
                    lk = k
                idx = line.rfind(k)
                if idx > ri:
                    ri = idx
                    rk = k
            s = s + (pattern.get(lk) * 10 + pattern.get(rk))
        Logger.info("Result=%d" % s)
