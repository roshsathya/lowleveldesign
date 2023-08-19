class Over:
    def __init__(self) -> None:
        self.total_balls = []
        self.bowler = None

    def add_ball(self, ball):
        self.total_balls.append(ball)

    def add_bowler(self, bowler):
        self.bowler = bowler
