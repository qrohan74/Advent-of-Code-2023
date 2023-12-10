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
        super().__init__(3, 1, self.go)

    def go(self):
        """
        Run puzzle
        """
        lines_without_numbers = [re.sub(r'\d', '.', s) for s in self.lines]
        res = 0
        for line_index, line in enumerate(self.lines):
            # find all numbers in the line
            line_numbers = re.findall(r'\d+', line)
            Logger.spam("Line %d: numbers are %s" % (line_index, line_numbers))

            # process each number in the line
            for line_number in line_numbers:
                index = line.index(line_number)
                length = len(line_number)
                is_part_number = False

                # check top
                if not is_part_number and line_index > 0:
                    a = 0 if index == 0 else index - 1
                    b = len(line) if index + length == len(line) else index + length + 1
                    s = lines_without_numbers[line_index - 1][a:b]
                    if s != len(s) * ".":
                        Logger.spam("Line %d: number %s is part number (top)" % (line_index, line_number))
                        is_part_number = True

                # check left
                if not is_part_number and index > 0 and lines_without_numbers[line_index][index - 1] != ".":
                    Logger.spam("Line %d: number %s is part number (left)" % (line_index, line_number))
                    is_part_number = True

                # check right
                if (not is_part_number and index + length < len(line) - 1
                        and lines_without_numbers[line_index][index + length] != "."):
                    Logger.spam("Line %d: number %s is part number (right)" % (line_index, line_number))
                    is_part_number = True

                # check bottom
                if not is_part_number and line_index < self.nb_lines - 1:
                    a = 0 if index == 0 else index - 1
                    b = len(line) if index + length == len(line) else index + length + 1
                    s = lines_without_numbers[line_index + 1][a:b]
                    if s != len(s) * ".":
                        Logger.spam("Line %d: number %s is part number (bottom)" % (line_index, line_number))
                        is_part_number = True

                # number processed, replace it with some '.' in the current line to avoid it being reused
                line = line.replace(line_number, "." * length, 1)

                # result
                if is_part_number:
                    res = res + int(line_number)

            # line processed, let's update it
            self.lines[line_index] = line
        Logger.info("Result=%d" % res)
