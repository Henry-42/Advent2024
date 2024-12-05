def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day4Input.txt")


def check_right(letter):
    if letter == "X":
        if x != 10:
            if grid[i][x + 1] == "M":
                return True
    if letter == "M":
        if x != 10:
            if grid[i][x + 1] == "A":
                return True
    if letter == "A":
        if x != 10:
            if grid[i][x + 1] == "S":
                return True
    return False


def check_left(letter):


grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

count = 0

for i in range(len(grid)):
    for x in range(len(grid[i])):
        print(grid[i][x])
