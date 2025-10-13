import re
from .game import Game

class LogParser:
    def __init__(self, log_path):
        self.log_path = log_path
        self.games = {}
        self.current_game = None
        self.game_count = 0

    def parse(self):
        with open(self.log_path, 'r') as file:
            for line in file:
                self._process_line(line.strip())

    def _process_line(self, line):
        if "InitGame:" in line:
            self._start_new_game()
        elif "Kill:" in line:
            self._process_kill(line)

    def _start_new_game(self):
        self.game_count += 1
        game_id = f"game_{self.game_count}"
        self.current_game = Game(game_id)
        self.games[game_id] = self.current_game

    def _process_kill(self, line):
        match = re.search(r'Kill: \d+ \d+ \d+: (.*?) killed (.*?) by', line)
        if match:
            killer, victim = match.groups()
            self.current_game.register_kill(killer, victim)

    def get_games(self):
        return {
            game_id: {
                "total_kills": game.total_kills,
                "players": sorted(list(game.players)),
                "kills": game.kills
            }
            for game_id, game in self.games.items()
        }
