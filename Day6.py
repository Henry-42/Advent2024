def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day6Input.txt")
print(file_data)


def get_answer(array):
    return array.split(":")[0]


def get_values(array):
    list_of_values = []
    arrayed = array.split(" ")
    arrayed.pop(0)
    # print(arrayed)
    for m in range(len(arrayed)):
        arrayed[m] = int(arrayed[m])

    for x in range(len(arrayed)):
        list_of_values.append(arrayed[x])
    return list_of_values

count = 0

for i in range(len(file_data)):
    print(get_answer(file_data[i]))
    print(get_values(file_data[i]))
    combination_index = len(get_values(file_data[i])) - 1

    for k in range(2**combination_index):
