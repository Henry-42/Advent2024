def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day4Input.txt")


def checking_xmas(pos):
    xmas_count = 0
    if pos == "X":
        if x != 0 and x != 9:
            if grid[i][x + 1] == "M":
                if x != 0:
                    if grid[i][x + 1] == "A":
                        if x != 0:
                            if grid[i][x + 1] == "S":
                                xmas_count += 1
        if i != 9:
            if grid[i - 1][x] == "M":
                if i != 9:
                    if grid[i - 1][x] == "A":
                        if i != 9:
                            if grid[i - 1][x] == "S":
                                xmas_count += 1
        if x != 0:
            if grid[i][x - 1] == "M":
                if x != 0:
                    if grid[i][x - 1] == "A":
                        if x != 0:
                            if grid[i][x - 1] == "S":
                                xmas_count += 1
        if x != 9:
            if grid[i][x+1] == "M":
                if x!=9:
                    if grid[i][x+1] == "A":
                        if x!=9:
                            if grid[i][x+1] =="S":
                                xmas_count+=1
        return xmas_count
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

count = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        checking_xmas(grid[row][col])
