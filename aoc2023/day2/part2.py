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
        super().__init__(2, 2, self.go)

    def go(self):
        """
        Run puzzle
        """
        s = 0
        for line in self.lines:
            min_nb_r = 0
            min_nb_g = 0
            min_nb_b = 0
            line_game, line_draws = [s.strip() for s in itemgetter(0, 1)(line.split(':'))]
            draws = [s.strip() for s in line_draws.split(';')]
            for draw in draws:
                balls = [s.strip() for s in draw.split(',')]
                for ball in balls:
                    if ball.endswith('red') and int(ball[:-4]) > min_nb_r:
                        min_nb_r = int(ball[:-4])
                    if ball.endswith('green') and int(ball[:-6]) > min_nb_g:
                        min_nb_g = int(ball[:-6])
                    if ball.endswith('blue') and int(ball[:-5]) > min_nb_b:
                        min_nb_b = int(ball[:-5])
            power = min_nb_r * min_nb_g * min_nb_b
            Logger.debug("%s power is %d" % (line_game, power))
            s = s + power
        Logger.info("Result=%d" % s)
