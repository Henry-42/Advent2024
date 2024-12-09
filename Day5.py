def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day5Input.txt")

rules = []
updates = []

for i in range(len(file_data)): # Use in if you want to
    if file_data[i].__contains__("|"):
        rules.append(file_data[i].split("|"))
    else:
        updates.append(file_data[i].split(","))

print(rules)
updates.pop(0) # Account for the space delimiter
print(updates)

count = 0

for i in range(len(updates)):
    listed_numbers = []
    for x in range(len(rules)):
        if rules[x][0] and rules[x][1] in updates[i]:
            listed_numbers.append(rules[x][0])
            listed_numbers.append(rules[x][1])
    for i in range(len(updates)):




