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
    for item in range(len(list_of_nums)):
        current_move = list_of_nums[item]
        if "forward" in current_move:
            x_pos = x_pos + int(current_move[-1])
            print(current_move, x_pos)
        elif "down" in current_move:
            y_pos = y_pos + int(current_move[-1])
            print(current_move, y_pos)
        elif "up" in current_move:
            print(y_pos)
            y_pos = y_pos - int(current_move[-1])
            print(current_move, y_pos)
        else:
            print("Something is wrong.")
    return x_pos * y_pos



# Track the submarine's journey through the depths with aim:
def sub_aim_location(list_of_nums):
    x_pos = 0
    y_pos = 0
    aim = 0
    for item in range(len(list_of_nums)):
        current_move = list_of_nums[item]
        magnitude = int(current_move[-1])
        if "forward" in current_move:
            x_pos = x_pos + magnitude
            y_pos = y_pos + (aim * magnitude)
            print(current_move, x_pos, aim)
        elif "down" in current_move:
            aim = aim + magnitude
            print(current_move, y_pos, aim)
        elif "up" in current_move:
            aim = aim - magnitude
            print(current_move, y_pos, aim)
        else:
            print("Something is wrong.")
    return x_pos * y_pos


# forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
# down 5 adds 5 to your aim, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
# up 3 decreases your aim by 3, resulting in a value of 2.
# down 8 adds 8 to your aim, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
test = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]

# print(locations)
print(sub_aim_location(locations))
