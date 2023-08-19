
from .batting_player import BattingPlayer
from .team import Team


class BattingTeam(Team):
    def __init__(self) -> None:
        self.players = {player: BattingPlayer(
            player) for player in self.players.keys()}
        self.on_strike_player = None
        self.off_strike_player = None

    def set_on_strike_player(self, player):
        temp = self.on_strike_player
        self.on_strike_player = self.players.get(player)
        self.off_strike_player = temp

    def add_player_score(self, player, score):
        current_player = self.players.get(player)
        current_player.add_score(score)

    def get_score(self):
        return sum(player.score for player in self.player.values())

    def get_batting_stats(self):
        return {
            player.name: {'score': player.score, 'is_batting': player.is_active} for player in self.players
        }
