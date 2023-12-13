from os import path

"""Example layout from github below"""
"""https://github.com/benediktwerner/AdventOfCode/blob/master/2023/day01/sol.py"""

def integer_conversion(list_item):
    try:
        integer = int(list_item)
        return(integer)
    except:
        return list_item

def data_part1(lines: list[str]):
        time = lines[0].split(" ")
        time = [i for i in time if i]
        time = list(map(integer_conversion, time))
             
        distance = lines[1].split(" ")
        distance = [i for i in distance if i]
        distance = list(map(integer_conversion, distance))
        return time, distance

def data_part2(lines: list[str]):
        time_str = ""
        time = lines[0].split(" ")
        time = [i for i in time if i]
        for item in time[1:]:
             time_str += item
        time = int(time_str)
        
        distance_str = ""
        distance = lines[1].split(" ")
        distance = [i for i in distance if i]
        for item in distance[1:]:
             distance_str += item
        distance = int(distance_str)

        count = 0
        for number in range(time):
            final_distance = (time - number) * number
            if final_distance > distance:
                    count += 1
        return count

def race(time, distance):
     number_of_wins = []
     for record in time[1:]:
          count = 0
          index = time.index(record)
          for number in range(record):
               final_distance = (record - number) * number
               if final_distance > distance[index]:
                    count += 1
          number_of_wins.append(count)

          print(record)
     return number_of_wins
     

def win_multiplication(number_of_wins):
    final_answer = 1
    for number in number_of_wins:
         final_answer = final_answer * number
    return final_answer


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    number_of_wins = race(data_part1(lines)[0], data_part1(lines)[1])
    final_answer = win_multiplication(number_of_wins)
    print("Part 1:", final_answer)

    print("Part 2:", data_part2(lines))