
from .bowling_player import BowlingPlayer
from .team import Team


class BowlingTeam(Team):
    def __init__(self) -> None:
        self.players = {player: BowlingPlayer(
            player) for player in self.players.keys()}
        self.current_bowler = None

    def set_current_bowler(self, player):
        self.current_bowler = self.players.get(player)

    def set_dismissal(self, type, batsman, bowler):
        current_player = self.players.get(batsman)
        current_player.add_dismissal(type, batsman, bowler)

    def get_bowling_stats(self):
        # This can be further computed to provide the top 3 or 5 bowlers
        return {player.name: {
            "wickets": player.wickets,
            "runs": player.runs
        } for player in self.players.values()}
