from os import path

"""Example layout from github below"""
"""https://github.com/benediktwerner/AdventOfCode/blob/master/2023/day01/sol.py"""

def solve(lines: list[str]):
    sum = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    game_dict = {}
    power = 0
    for line in lines:
        line = line.split(":")
        game_dict[line[0]] = line[1]

    for game in game_dict.values():
        min_red = 0
        min_green = 0
        min_blue = 0
        fail = False
        rounds = game.split(";")
        for round in rounds:
            colors = round.split(",")
            for color in colors:
                if "red" in color:
                    color = color.split(" ")
                    if int(color[1]) > min_red:
                        min_red = int(color[1])
                    if int(color[1]) > max_red:
                        fail = True
                if "blue" in color:
                    color = color.split(" ")
                    if int(color[1]) > min_blue:
                        min_blue = int(color[1])
                    if int(color[1]) > max_blue:
                        fail = True
                if "green" in color:
                    color = color.split(" ")
                    if int(color[1]) > min_green:
                        min_green = int(color[1])
                    
                    if int(color[1]) > max_green:
                        fail = True
        if fail == False:
            val_list = list(game_dict.values())
            key_list = list(game_dict.keys())
            position = val_list.index(game)
            winning_game = key_list[position]
            game_value = winning_game.split(" ")
            sum += int(game_value[1])
        
        power += min_red * min_green * min_blue
        #print(rounds)
    return sum, power

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    print("Part 1:", solve(lines))
    #print("Part 2:", solve(lines, max))