from parser.log_parser import LogParser

def main():
    parser = LogParser("data/games.log")
    parser.parse()
    games = parser.get_games()

    for game_id, data in games.items():
        print(f"\n{game_id}:")
        print(data)

    ranking = {}
    for game in games.values():
        for player, kills in game["kills"].items():
            ranking[player] = ranking.get(player, 0) + kills

    ranking_sorted = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    print("\n🏆 RANKING GERAL 🏆")
    for player, kills in ranking_sorted:
        print(f"{player}: {kills} kills")

if __name__ == "__main__":
    main()
