# Advent of Code Day 3
# Solution by Dev Sodagar
# 2021-12-03

diagnostic = []

# Read in text file and convert to a list
with open("input3.txt", "r", encoding="UTF-8") as file:
    while line := file.readline().rstrip():
        diagnostic.append(line)


# Convert simple list into a 2d array:
def list_to_2dlist(list_of_nums):
    report_array = []
    for item in range(len(list_of_nums)):
        report_line = list_of_nums[item]
        row = []
        for element in report_line:
            row.append(int(element))
        report_array.append(row)
    return report_array


# Convert simple list into a pivoted array:
# def list_to_inv_list(list_of_nums):
#     report_array = []
#     for item in range(len(list_of_nums)):
#         report_array.append(list_of_nums[item].pop(0))
#     print(report_array)


# Convert simple list into a pivoted array:
def bin_array_to_decimal(list_of_bins):
    dec_val = 0
    length = len(list_of_bins)
    for item in range(len(list_of_bins)):
        if list_of_bins[item] == 1:
            dec_val = dec_val + (2 ** (length - (item + 1)))
    # print(dec_val)
    return dec_val


# Calculate the power consumption from sub diagnostic report:
def power_consumption(list_of_nums):
    report_array = list_to_2dlist(list_of_nums)
    length = len(list_of_nums)
    gamma = []
    epsilon = []
    for time in range(len(report_array[1])):
        i = 0
        for row in report_array:
            i = i + row.pop(0)
        gamma_digit = round(i / length)
        if gamma_digit == 1:
            epsilon.append(0)
            gamma.append(1)
        else:
            epsilon.append(1)
            gamma.append(0)
    print(gamma, epsilon)
    power = bin_array_to_decimal(gamma) * bin_array_to_decimal(epsilon)
    print(power)


# Calculate the power consumption from sub diagnostic report:
def air_consumption(list_of_nums):
    report_array = list_to_2dlist(list_of_nums)
    length = len(list_of_nums)
    oxy = []
    co2 = []
    for time in range(len(report_array[1])):
        i = 0
        for row in report_array: ### ###
            i = i + row.pop(0)
        oxy_digit = round(i / length)
        report_array = report_array where report_array[][time] = oxy_digit
    print(oxy, co2)
    power = bin_array_to_decimal(oxy) * bin_array_to_decimal(co2)
    print(power)


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


test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

test2 = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0]
]


# print(diagnostic)
print(power_consumption(diagnostic))
# print(list_to_2dlist(diagnostic))
