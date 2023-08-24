

class ScoreCard:
    def __init__(self, game) -> None:
        self.game = game

    def get_current_score(self):
        return self.game.get_score()

    def get_current_batsman(self):
        batting_team = self.game.current_batting
        return {
            batting_team.on_strike_player.name: batting_team.on_strike_player.score,
            batting_team.off_strike_player.name: batting_team.off_strike_player.score,
        }

    def get_current_bowler(self):
        bowling_team = self.game.current_bowling
        return {
            bowling_team.current_player.name: {
                "runs_conceded": bowling_team.current_player.score,
                "wickets": len(bowling_team.current_player.wickets)
            }
        }

    def get_current_batting_score(self):
        return self.game.current_batting.get_batting_stats()

    def get_current_bowling_score(self):
        return self.game.current_bowling.get_bowling_stats()
