class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.total_kills = 0
        self.players = set()
        self.kills = {}

    def add_player(self, player):
        if player not in self.kills:
            self.kills[player] = 0
            self.players.add(player)

    def register_kill(self, killer, victim):
        self.total_kills += 1

        if killer == "<world>":
            if victim in self.kills:
                self.kills[victim] -= 1
            return

        self.add_player(killer)
        self.add_player(victim)
        self.kills[killer] += 1
