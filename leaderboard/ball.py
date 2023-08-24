class Ball:
    def __init__(self, batsman, bowler) -> None:
        self.bowler = bowler
        self.batsman = batsman
        self.runs = 0
        self.dismissal = None

    def add_runs(self, runs):
        self.runs = runs
        self.batsman.add_score(self.bowler, runs)
        self.bowler.add_score(self.batsman, runs)

    def add_dismissal(self, dismissal):
        self.dismissal = dismissal
