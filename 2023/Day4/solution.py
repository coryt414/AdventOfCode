from os import path

"""Example layout from github below"""
"""https://github.com/benediktwerner/AdventOfCode/blob/master/2023/day01/sol.py"""

def solve1(lines: list[str]):
    total = 0
    print(lines[0])
    for line in lines:
        round_score = 0
        line = line.split(":")
        line = line[1].split("|")
        winning_numbers = line[0].strip(" ")
        winning_numbers = winning_numbers.split(" ")
        winning_numbers = [x for x in winning_numbers if x!='']
        my_numbers = line[1].strip(" ")
        my_numbers = my_numbers.split(" ")
        my_numbers = [x for x in my_numbers if x!='']

        for number in winning_numbers:
            if number in my_numbers and round_score == 0:
                round_score += 1
            elif number in my_numbers and round_score > 0:
                round_score = round_score * 2
        total += round_score

    #print(winning_numbers, my_numbers)
    return total

def solve2(lines: list[str]):
    final_cards = []
    total = 0
    line = ""
    for i in range(len(lines)):
        round_score = 0
        line = lines[i].split(":")
        line = line[1].split("|")
        winning_numbers = line[0].strip(" ")
        winning_numbers = winning_numbers.split(" ")
        winning_numbers = [x for x in winning_numbers if x!='']
        my_numbers = line[1].strip(" ")
        my_numbers = my_numbers.split(" ")
        my_numbers = [x for x in my_numbers if x!='']

        for number in winning_numbers:
            #if number in my_numbers and round_score == 0:
            #    lines.append(lines[i])
                #round_score += 1
            if number in my_numbers:
                round_score += 1
        for j in range(i + 1, i + 1 + round_score):
            lines.append(lines[j])
        lines.sort()
        total += round_score

    total = 0
    for line in final_cards:
        round_score = 0
        line = line.split(":")
        line = line[1].split("|")
        winning_numbers = line[0].strip(" ")
        winning_numbers = winning_numbers.split(" ")
        winning_numbers = [x for x in winning_numbers if x!='']
        my_numbers = line[1].strip(" ")
        my_numbers = my_numbers.split(" ")
        my_numbers = [x for x in my_numbers if x!='']

        for number in winning_numbers:
            if number in my_numbers and round_score == 0:
                round_score += 1
            elif number in my_numbers and round_score > 0:
                round_score = round_score * 2
        total += round_score
    print(len(lines))
    return total

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    print("Part 1:", solve1(lines))
    print("Part 2:", solve2(lines))