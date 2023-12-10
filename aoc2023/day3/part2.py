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

    def look_for_part_numbers(self, row, column):
        """
        Return the list of numbers connected to a given column index
        The returned list can be either empty, or a list of 1 or 2 elements
        """
        part_numbers = []

        # check each number of the top line
        line = self.lines[row]
        line_numbers = re.findall(r'\d+', line)
        for line_number in line_numbers:
            index = line.index(line_number)
            length = len(line_number)

            # check connection
            a = 0 if index == 0 else index - 1
            b = len(line) if index + length == len(line) else index + length
            if a <= column <= b:
                part_numbers.append(int(line_number))

            # number processed, replace it with some '.' in the current line to avoid it being reused
            line = line.replace(line_number, "." * length, 1)
        return part_numbers

    def go(self):
        """
        Run puzzle
        Note: this function does not check the weird case where 2 part numbers are connected with more than one gear.
        Example:
            ...127....
            ...*.*....
            ....428...
        Such gear configurations would not work
        """
        lines_without_numbers = [re.sub(r'\d', '.', s) for s in self.lines]
        res = 0
        for line_index, line in enumerate(self.lines):
            # loop over the gears of the line
            while "*" in line:
                line_column = line.index("*")
                part_numbers = []
                # check top
                if line_column > 0:
                    part_numbers.extend(self.look_for_part_numbers(line_index - 1, line_column))
                # check bottom
                if line_column < self.nb_lines - 1:
                    part_numbers.extend(self.look_for_part_numbers(line_index + 1, line_column))
                # check left, right
                part_numbers.extend(self.look_for_part_numbers(line_index, line_column))
                if len(part_numbers) > 2:
                    Logger.warning(
                        "Line %d: more than 2 part numbers connected to same gear (%s)" % (line_index, part_numbers))
                if len(part_numbers) == 2:
                    Logger.debug("Line %d: gear connection found (%s)" % (line_index, part_numbers))
                    res = res + (part_numbers[0] * part_numbers[1])
                # gear processed, replace it with a '.' in the current line to avoid it being reused
                line = line.replace("*", ".", 1)
        Logger.info("Result=%d" % res)
