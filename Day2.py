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

    # checks if the input is decreasing/increasing; if not set to false.
    for i in range(len(array) - 1):
        if int(array[i]) > int(array[i + 1]):
            inc = False
        if int(array[i]) < int(array[i + 1]):
            dec = False

    # if its increasing/decreasing throughout returns True
    if dec:
        return True
    if inc:
        return True

    # returns false otherwise
    return False


def adj_tof(inputs):
    array = inputs.split(" ")
    for i in range(len(array) - 1):

        # Checks the difference between the two.
        difference = abs(int(array[i + 1]) - int(array[i]))

        # early return of false when difference is not in the specified range
        if difference < 1 or difference > 3:
            return False
    # returns true if the distance is in between throughout
    return True


file_data = get_file_data("Day2Input.txt")

part_one_answer = 0

for element in file_data:
    if adj_tof(element) and increasing_or_decreasing(element):
        part_one_answer += 1


print(part_one_answer)


# Part 2


def adj_tof_p2(inputs):
    # removal of split to help with the other function; same usage otherwise

    for i in range(len(inputs) - 1):
        difference = abs(int(inputs[i + 1]) - int(inputs[i]))
        if difference < 1 or difference > 3:
            return False
    return True


def increasing_or_decreasing_p2(inputs):
    # removal of split to help with the other function; same usage otherwise

    inc = True
    dec = True

    for i in range(len(inputs) - 1):
        if int(inputs[i]) > int(inputs[i + 1]):
            inc = False
        if int(inputs[i]) < int(inputs[i + 1]):
            dec = False

    if dec:
        return True
    if inc:
        return True

    return False


def one_or_more(elements):
    place_holder = elements.split(" ")
    for i in range(len(place_holder)):

        # remakes array everytime to ensure only one thing is being popped while other elements remain the same
        array = place_holder.copy()
        array.pop(i)

        # returns early true if one of the elements are popped and returns true with the helper methods
        if adj_tof_p2(array) and increasing_or_decreasing_p2(array):
            return True

        # if all elements are popped and none return true returns false
    return False


count = 0

for x in file_data:
    if increasing_or_decreasing(x) and adj_tof(x) or one_or_more(x):
        count += 1

print(count)
