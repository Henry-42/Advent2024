def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def get_middle_number(list2):
    return list2[round(len(list2) / 2)]


file_data = get_file_data("Day5Input.txt")

rules = []
updates = []

for i in range(len(file_data)):  # Use in if you want to
    if file_data[i].__contains__("|"):
        rules.append(file_data[i].split("|"))
    else:
        updates.append(file_data[i].split(","))

print(rules)
updates.pop(0)  # Account for the space delimiter
print(updates)

count = 0

for i in range(len(updates)):
    tor = True
    listed_numbers = []
    for x in range(len(rules)):
        if rules[x][0] and rules[x][1] in updates[i]:
            temp_list = (rules[x][0], rules[x][1])
            listed_numbers.append(temp_list)
    for z in range(len(listed_numbers)):
            pos = 0
            pos2 = 0
            if updates[i] == listed_numbers[z][0]:
                pos = i
            if updates[i] == listed_numbers[z][1]:
                pos2 = i
            if pos > pos2:
                tor = False

    if tor:
        count += int(get_middle_number(updates[i]))

print(count)
