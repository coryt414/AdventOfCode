sum = 0
index = 1
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers_dict = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
    }
with open("2023/Day_1_input.txt", "r") as file:
    for line in file:
        coordinate = ""
        for i in range(len(line)):
            if line[i].isdigit():
                coordinate += (line[i])
            j = i
            while j in range(len(line)):
                if line[i:j] in numbers_dict.keys():
                    value = numbers_dict[line[i:j]]
                    coordinate += str(value)    
                    break
                else:
                    j += 1
        coordinate = coordinate[0] + coordinate[-1]
        print(index, coordinate)
        sum += int(coordinate)
        index += 1
print(sum)