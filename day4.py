# Advent of Code Day 4
# Solution by Dev Sodagar
# 2021-12-04

#Bingo draws
Guess = [42,32,13,22,91,2,88,85,53,87,37,33,76,98,89,19,69,9,62,21,38,49,54,81,0,26,79,36,57,18,4,40,31,80,24,64,77,
         97,70,6,73,23,20,47,45,51,74,25,95,96,58,92,94,11,39,63,65,99,48,83,29,34,44,75,55,17,14,56,8,82,59,52,46,
         90,5,41,60,67,16,1,15,61,71,66,72,30,28,3,43,27,78,10,86,7,50,35,84,12,93,68]

bingo_input = []

# Read in text file and convert to a list
with open("input4.txt", "r", encoding="UTF-8") as file:
    while line := file.readline().rstrip():
        bingo_input.append(line)


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

test2 = [[
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1]],
    [[0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1]]
]

def array_transposition(array):
    new_array = []
    for col_num in range(len(array[0])):
        new_row = []
        for row in array:
            new_row.append(row[col_num])
        new_array.append(new_row)
    return new_array


# Adds transposed data to original data as additional bingo cards
def card_pivot(array):
    new_array = array
    for card in range(len(array)):
        new_card = array_transposition(array[card])
        new_array.append(new_card)
    print(new_array)


# Runs the bingo game by checking all bingo cards against the bingo call and returning the winning number.
def bingo_game(array, bingo_nums):
    for call in bingo_nums:




# card_pivot(test2)
print(list_to_2dlist(bingo_input))
