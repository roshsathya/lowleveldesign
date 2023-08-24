from player import Player


class BattingPlayer(Player):
    def __init__(self, name, country) -> None:
        super().__init__(name, country)
        self.score = 0
        self.dismissal = None
        self.active = False
        self.bowler = {}

    def add_score(self, bowler, score):
        if bowler not in self.bowler:
            self.bowler[bowler] += score
        self.score += score

    def add_dismissal(self, dismissal):
        self.dismissal = dismissal
