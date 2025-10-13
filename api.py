from flask import Flask, jsonify
from parser.log_parser import LogParser

app = Flask(__name__)
parser = LogParser("data/games.log")
parser.parse()
games = parser.get_games()

@app.route("/games/<game_id>", methods=["GET"])
def get_game(game_id):
    if game_id in games:
        return jsonify(games[game_id])
    return jsonify({"error": "Game not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
