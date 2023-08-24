from .over import Over
from .dismissal import DismissalFactory


class Game:
    def __init__(self, team1_batting, team2_batting, team1_bowling, team2_bowling, total_overs) -> None:
        self.team1_batting = team1_batting
        self.team2_batting = team2_batting
        self.team1_bowling = team1_bowling
        self.team2_bowling = team2_bowling
        self.overs = [Over() for _ in range(total_overs)]
        self.current_over = 0
        self.current_batting = None
        self.current_bowling = None

    def get_score(self):
        second_team = self.team2_batting if self.current_batting == self.team1_batting else self.team1_batting
        return {
            self.current_batting.name: self.current_batting.get_score(),
            second_team.name: second_team.get_score()
        }

    def set_current_batting(self, team):
        if team.name == self.team1_batting:
            self.current_batting = self.team1_batting
            self.current_bowling = self.team2_bowling
        else:
            self.current_batting = self.team2_batting
            self.current_bowling = self.team1_bowling

    def add_score(self, batsman, bowler, score):
        if batsman not in self.current_batting or bowler not in self.current_bowling:
            raise Exception()
        self.overs[self.current_over].add_ball(score, batsman, bowler)

    def add_dismissal(self, dismissal_type, batsman, bowler):
        if batsman not in self.current_batting or bowler not in self.current_bowling:
            raise Exception()
        dismissal = DismissalFactory.get_dismissal(
            dismissal_type, self, bowler)
        batsman.add_dismissal(dismissal)
        bowler.add_dismissal(dismissal)

    def next_over(self, bowler):
        self.current_over += 1
        self.overs[self.current_over].add_bowler(bowler)
