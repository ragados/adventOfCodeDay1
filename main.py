# Advent of Code Day 1
# Solution by Dev Sodagar
# 2021-12-01

depths = []

# Read in text file and convert to a list
with open("input.txt", "r", encoding="UTF-8") as file:
    while (line := file.readline().rstrip()):
        depths.append(line)

# Take a list and iterate through it. Increment depth_measure_increment where depth increases
def increase_counter(list):
    depth_measure_increase = 0
    for item in range(len(list)):
        if list[item] > list[item-1]:
            depth_measure_increase += 1
    return depth_measure_increase


print(increase_counter(depths))
