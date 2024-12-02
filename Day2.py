def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


# PART 1

def increasing_or_decreasing(inputs):
    array = inputs.split(" ")
    inc = True
    dec = True

    for i in range(len(array) - 1):
        if int(array[i]) > int(array[i+1]):
            inc = False
        if int(array[i]) < int(array[i+1]):
            dec = False

    if dec:
        return True
    if inc:
        return True

    return False

def adj_tof(inputs):
    array = inputs.split(" ")
    for i in range(len(array) - 1):
        difference = abs(int(array[i + 1]) - int(array[i]))
        if difference < 1 or difference > 3:
            return False
    return True


file_data = get_file_data("Day2Input.txt")

count = 0

for element in file_data:
    if adj_tof(element) and increasing_or_decreasing(element):
        count+=1

print(count)

# Part 2






