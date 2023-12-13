from os import path

"""Example layout from github below"""
"""https://github.com/benediktwerner/AdventOfCode/blob/master/2023/day01/sol.py"""

def navigate(dir, coords):
    value = coords[1][0:3]
    count = 0
    finish = "ZZZ"

    for letter in dir:
        if letter == "L":
            for coord in coords:
                if coord[0:3] == value:
                    value = coord[-9:-6]
                    count += 1
                    if value == "ZZZ":
                        print(count)
                    #print(value)
                    break
        if letter =="R":
            for coord in coords:
                if coord[0:3] == value:
                    value = coord[-4:-1]
                    count += 1
                    if "ZZZ" == value:
                        print(count)
                    #print(value)
                    break



        #print("RIGHT: ", right)
        #print("LEFT: ", left)
    #print(coords)
    return

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    data = f.read()
    dir, *coords = data.split("\n")
    dir = dir*500
    coords.sort()
    #print(dir)
    #print(*coords, sep='\n')
    navigate(dir, coords)
    #print("Part 2:", solve(lines, max))