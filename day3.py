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


# Calculate the air consumption from sub diagnostic report:
def air_consumption(list_of_nums):
    report_array = list_to_2dlist(list_of_nums)
    oxy = report_array
    co2 = report_array
    # Oxygen calculation
    for col_num in range(len(report_array[1])):
        i = 0
        oxy_array = []
        for row in oxy:
            i = i + row[col_num]
        length = len(oxy)
        if (i / length) == 0.5:
            oxy_digit = 1
        else:
            oxy_digit = round(i / length)
#        report_array = [row for row in report_array if row[time] == oxy_digit]
        for row in oxy:
            if row[col_num] == oxy_digit:
                oxy_array.append(row)
        oxy = oxy_array
        if len(oxy) == 1:
            continue
    #CO2 calculation
    for col_num in range(len(report_array[1])):
        i = 0
        co2_array = []
        for row in co2:
            i = i + row[col_num]
        length = len(co2)
        if (i / length) == 0.5:
            co2_digit = 1
        else:
            co2_digit = round(i / length)
        print(i, length)
        print("Digit: ", co2_digit)
        for row in co2:
            if row[col_num] != co2_digit:
                co2_array.append(row)
        co2 = co2_array
        print(co2)
        if len(co2) == 1:
            break
    print("Oxy: ", oxy)
    print("CO2: ", co2)
    power = bin_array_to_decimal(oxy[0]) * bin_array_to_decimal(co2[0])
    print("Power: ", power)


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
air_consumption(diagnostic)
# print(list_to_2dlist(diagnostic))
