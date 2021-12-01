# Advent of Code Day 1
# Solution by Dev Sodagar
# 2021-12-01

depths = []

# Read in text file and convert to a list
with open("input.txt", "r", encoding="UTF-8") as file:
    while line := file.readline().rstrip():
        depths.append(int(line))


# Take a list and iterate through it. Increment depth_measure_increment where depth increases
def increase_counter(list_of_nums):
    depth_measure_increase = 0
    for item in range(1, len(list_of_nums)):
        if list_of_nums[item] > list_of_nums[item - 1]:
            depth_measure_increase += 1
            print(list_of_nums[item], depth_measure_increase, list_of_nums[item-1])
    return depth_measure_increase


# Take a list and iterate through it. Increment depth_measure_increment where depth of a 3 point avg increases
def mv_avg_increase_counter(list_of_nums):
    depth_measure_increase = 0
    for item in range(3, len(list_of_nums)):
        current = list_of_nums[item] + list_of_nums[item - 1] + list_of_nums[item - 2]
        previous = list_of_nums[item - 1] + list_of_nums[item - 2] + list_of_nums[item - 3]
        if current > previous:
            depth_measure_increase += 1
    return depth_measure_increase


test = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
    180
]

print(mv_avg_increase_counter(depths))
