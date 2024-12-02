def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day1Input.txt")

# Part 1

splits = []
list1 = []
list2 = []
distance = 0

def list_splitting(file_data):

    # splits file_data into pairs of numbers one and two
    for data in file_data:
        item1 = data.split("   ")
        splits.append(item1)

    # separates numbers one and two into their respective arrays
    for element in splits:
        list1.append(element[0])
        list2.append(element[1])

    list1.sort()
    list2.sort()

list_splitting(file_data)

for i in range(len(list1)):
    distance += (abs(int(list1[i]) - int(list2[i])))


print(distance)

# Part 2

similarity_score = 0

for x in list1:

        count = 0
        num = int(x)

        for z in list2:
            if x == z:
                count+=1

        similarity_score += num * count

print(similarity_score)




