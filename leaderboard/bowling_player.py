from .dismissal import DismissalFactory
from player import Player


class BowlingPlayer(Player):
    def __init__(self, name, country) -> None:
        super().__init__(name, country)
        self.score = 0
        self.batsman = {}
        self.wickets = []

    def add_score(self, batsman, score):
        if batsman not in self.batsman:
            self.batsman = {batsman: 0}
        self.batsman[batsman] += score
        self.score += score

    def add_dismissal(self, dismissal):
        self.wickets.append(dismissal)
