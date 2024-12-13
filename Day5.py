def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def get_middle_number(list2):
    print(list2[round(len(list2) // 2)])
    return list2[round(len(list2) // 2)]


def rule_followed():
    pos = 0
    pos2 = 0
    for z in range(len(listed_numbers)):
        for m in range(len(updates[i])):
            if updates[i][m] == listed_numbers[z][0]:
                pos = m

            if updates[i][m] == listed_numbers[z][1]:
                pos2 = m

        if pos > pos2:
            return False
    return True


def rule_followed_part_two(list):
    pos = 0
    pos2 = 0
    for z in range(len(listed_numbers)):
        for m in range(len(list)):
            if list[i][m] == listed_numbers[z][0]:
                pos = m

            if list[i][m] == listed_numbers[z][1]:
                pos2 = m

        if pos > pos2:
            return False
    return True


def temporary_list():
    pos = 0
    pos2 = 0
    for z in range(len(listed_numbers)):
        for m in range(len(updates[i])):
            if updates[i][m] == listed_numbers[z][0]:
                pos = m
            if updates[i][m] == listed_numbers[z][1]:
                pos2 = m

        if pos > pos2:
            temp = temp_list_two[i][pos]
            temp2 = temp_list[i][pos2]
            temp_list_two[i][pos] = temp2
            temp_list_two[i][pos2] = temp
    return temp_list_two

file_data = get_file_data("Day5Input.txt")

rules = []
updates = []

for i in range(len(file_data)):  # Use in if you want to
    if file_data[i].__contains__("|"):
        rules.append(file_data[i].split("|"))
    else:
        updates.append(file_data[i].split(","))

# print(rules)
updates.pop(0)  # Account for the space delimiter
print(updates)

count = 0

for i in range(len(updates)):
    listed_numbers = []
    for x in range(len(rules)):
        if rules[x][0] in updates[i]:
            if rules[x][1] in updates[i]:
                temp_list = (rules[x][0], rules[x][1])
                listed_numbers.append(temp_list)

    torf = rule_followed()

    if torf:
        count += int(get_middle_number(updates[i]))

print(count)

# Part 2

list_of_incorrect = []
count_two = 0

for i in range(len(updates)):
    temp_list_two = updates[i]
    listed_numbers = []
    for x in range(len(rules)):
        if rules[x][0] in updates[i]:
            if rules[x][1] in updates[i]:
                temp_list = (rules[x][0], rules[x][1])
                listed_numbers.append(temp_list)
    torf = rule_followed()

    if not torf:
        list_of_incorrect.append(updates[i])
        print(listed_numbers)

    while not torf:
        torf = rule_followed_part_two(temporary_list())

    count_two += int(get_middle_number(updates[i]))
print(list_of_incorrect)
print(count_two)
