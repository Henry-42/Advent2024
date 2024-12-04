import re


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day3Input.txt")

# Joining strings as file_data is a list & re.findall needs a singular string.
joined_strings = ' '.join(file_data)

#mul matches mul;
# \( matches the literal parenthesis;
# (\d+) captures the group of the digit (\d) from [0-9];
# and the + repeats for as long as possible;
# , is the literal
# another capture group of (\d+)
# \) string literal of parenthesis
regex = "mul\((\d+),(\d+)\)"
matches = re.findall(regex, joined_strings)
print(matches)

# checking type of returned list
print(type(matches[0]))

count = 0

for i in range(len(matches)):
    # since the returned matches are a list of tuples, we can access the first and second elements directly as it is.
    integer_one = int(matches[i][0])
    integer_two = int(matches[i][1])
    mul = integer_one * integer_two
    count += mul

print(count)

# PART 2

regex_p2 = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches_p2 = re.findall(regex_p2, joined_strings)
print((matches_p2))

count_p2 = 0

allowed = True

for i in range(len(matches_p2)):
    if matches_p2[i] == "don't()":
        allowed = False
    if matches_p2[i] == "do()":
        allowed = True
    if allowed:
        if matches_p2[i] != "don't()" and matches_p2[i] != "do()":
            list_of_integers = matches_p2[i].strip("mul()").split(",")
            print(list_of_integers)
            integer_one_p2 = list_of_integers[0]
            print(integer_one_p2)
            integer_two_p2 = list_of_integers[1]
            print(integer_two_p2)
            count_p2 += int(integer_one_p2) * int(integer_two_p2)
            list_of_integers = matches_p2[i].strip("mul()").split(",")

print(count_p2)
