from .player import Player


class Team:
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country
        self.players = {}

    def add_players(self, name):
        self.players[name] = Player(name, self.country)
