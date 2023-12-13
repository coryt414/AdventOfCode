from os import path
import json
"""Example layout from github below"""
"""https://github.com/benediktwerner/AdventOfCode/blob/master/2023/day01/sol.py"""

def data_structure(lines: list[str]):
    seeds, *data_blocks = lines.split("\n\n")
    
    #print(data_blocks)
    seeds = list(map(int, seeds.split(":")[1].split()))

    for datablock in data_blocks:
        print(datablock)
        print("\n\n\n\n\n\n")
    print(seeds)
    """seeds = []
    for line in lines:
        #line = line.split("\n")
        # seeds ID

        if "seeds" in line:
            line = line[0].split(" ")
            for item in line:
                if item.isdigit():
                    seeds.append(item)

        elif line != "" and line[0].isalpha():
            map = []
            index = lines.index(line)
            while lines[index] != "":
                map.append(line)
                index += 1
            print(map)"""



def seed_to_soil_map(lines: list[str]):
    
    return

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read()
    data_structure(lines)
    #print("Part 1:", solve(lines))
    #print("Part 2:", solve(lines, max))