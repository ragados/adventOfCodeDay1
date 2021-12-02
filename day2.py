# Advent of Code Day 1
# Solution by Dev Sodagar
# 2021-12-01

locations = []

# Read in text file and convert to a list
with open("input2.txt", "r", encoding="UTF-8") as file:
    while line := file.readline().rstrip():
        locations.append(line)


# Track the submarine's journey through the depths:
def sub_location(list_of_nums):
    x_pos = 0
    y_pos = 0
    for item in range(1, len(list_of_nums)):
        if forward:
            x_pos = x_pos + value
            print(list_of_nums[item], x_pos,)
        elif down:
            y_pos = y_pos + value
            print(list_of_nums[item], y_pos)
        elif up:
            y_pos = y_pos - value
            print(list_of_nums[item], y_pos)
        else:
            print("Something is wrong.")
    return x_pos * y_pos

print(locations)
# print(sub_location(depths))