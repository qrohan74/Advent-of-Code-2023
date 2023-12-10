import re
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
        super().__init__(4, 2, self.go)
        self.total_cards = 0
        self.total_cards = 0

    def get_score(self, card_id):
        """
        get the score of a card
        """
        line_card, line_values = [s.strip() for s in itemgetter(0, 1)(self.lines[card_id].split(':'))]
        line_winning, line_draw = [s.strip() for s in itemgetter(0, 1)(line_values.split('|'))]
        card_score = len(list(set([int(n) for n in re.findall(r'\d+', line_winning)]).intersection(
            [int(n) for n in re.findall(r'\d+', line_draw)])))
        Logger.spam("%s: score=%d" % (line_card, card_score))
        return card_score

    def scratch_card(self, scores, card_id):
        """
        a recursive method to scratch a card. This just increments the card counter, then scratch the won copies
        """
        self.total_cards += 1
        for n in range(scores[card_id]):
            self.scratch_card(scores, card_id + n + 1)

    def go(self):
        """
        Run puzzle
        """
        scores = [self.get_score(n) for n in range(self.nb_lines)]
        for line_index, line in enumerate(self.lines):
            Logger.debug("Scratch original card %d" % (line_index + 1))
            self.scratch_card(scores, line_index)
        Logger.info("Result=%d" % self.total_cards)
