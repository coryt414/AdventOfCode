from os import path

"""Example layout from github below"""
"""https://github.com/benediktwerner/AdventOfCode/blob/master/2023/day01/sol.py"""

exclude = ["0","1","2","3","4","5","6","7","8","9","."]

def solve(lines: list[str]):
    sum = 0
    for y_coord in range(len(lines)):
        x_coord = 0
        while x_coord in range(len(lines[y_coord])):
            number = ""
            index = []
            try:
                while lines[y_coord][x_coord].isdigit():
                    number += lines[y_coord][x_coord]
                    index.append(x_coord)
                    x_coord += 1
                if number != "":
                    index.append(index[-1]+1)
                    index.append(index[0]-1)
                    print(index)
                    for item in index:
                        print(lines[y_coord+1])
                        print(lines[y_coord-1][item-1], lines[y_coord][item-1], lines[y_coord+1][item])
                        try:
                            if lines[y_coord-1][item-1] not in exclude:
                                sum += int(number)
                        except:
                            pass
                        try:
                            if lines[y_coord][item-1] not in exclude:
                                sum += int(number)
                        except:
                            pass
                        try:
                            if lines[y_coord+1][item] not in exclude:
                                print(lines[y_coord+1][item-1])
                                sum += int(number)
                        except:
                            pass

                if number == "":
                    x_coord += 1
            except:
                pass
    return sum



with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    print("Part 1:", solve(lines))
    #print("Part 2:", solve(lines, max))