def get_input(filename):
    changes = []
    file = open(filename)
    for line in file:
        line = int(line[:-1])
        changes.append(line)
    file.close()
    return changes


def get_resulting_frequency(my_list):
    sum_of_frequencies = 0
    for x in my_list:
        sum_of_frequencies = sum_of_frequencies + x
    return sum_of_frequencies


def get_first_repeating_frequency(my_list):
    number_of_elements = len(my_list)
    sum_of_frequencies = 0
    frequencies_set = set([])
    index = 0
    while True:

        index = index % number_of_elements
        sum_of_frequencies = sum_of_frequencies + my_list[index]
        if sum_of_frequencies in frequencies_set:
            break

        frequencies_set.add(sum_of_frequencies)
        index = index + 1
    return sum_of_frequencies


changes = get_input('2018/Day1/input.txt')
print("Resulting frequency (part 1) = {}".format(get_resulting_frequency(changes)))
print("First frequency reached twice(part 2) = {}".format(get_first_repeating_frequency(changes)))