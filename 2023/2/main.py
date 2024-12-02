import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

games: dict[int, list[dict[str, int]]] = {}
for line in lines:
    game, rounds = line.split(":", maxsplit=1)
    _, game_number = game.split(" ")
    games[int(game_number)] = []
    rounds = rounds.split(";")
    for it in rounds:
        next_round = {}
        balls = it.strip().split(",")
        for ball in balls:
            number, color = ball.strip().split(" ")
            next_round[color] = int(number)
        games[int(game_number)].append(next_round)


def _validate_round(round_: dict[str, int]):
    for color, number in round_.items():
        if color == "red" and number > 12:
            return False
        if color == "green" and number > 13:
            return False
        if color == "blue" and number > 14:
            return False
    return True


result = 0
for game_number, game in games.items():
    if all(_validate_round(it) for it in game):
        result += game_number
print(f"Part 1: {result}")


def _cubes_power(game: list[dict[str, int]]):
    min_red = max(*[it["red"] if "red" in it else 0 for it in game])
    min_green = max(*[it["green"] if "green" in it else 0 for it in game])
    min_blue = max(*[it["blue"] if "blue" in it else 0 for it in game])
    return min_red * min_green * min_blue


result = 0
for game_number, game in games.items():
    result += _cubes_power(game)
print(f"Part 2: {result}")
