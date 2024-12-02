def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day1Input.txt")

# Part 1

Split = []
List1 = []
List2 = []
Distance = 0
for x in file_data:
    item1 = x.split("   ")
    Split.append(item1)

for x in Split:
    List1.append(x[0])
    List2.append(x[1])

List1.sort()
List2.sort()


for i in range(len(List1)):
    Distance += (abs(int(List1[i]) - int(List2[i])))

print(Distance)

# Part 2