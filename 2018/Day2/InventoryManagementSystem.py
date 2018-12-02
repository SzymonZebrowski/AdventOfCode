def get_input(filename):
    changes = []
    with open(filename) as file:
        for line in file:
            line = line[:-1]
            changes.append(line)
    return changes


def count_letters_of_id(box_id):
    letters_set = set(box_id)
    dictionary = {x: 0 for x in letters_set}

    for x in box_id:
        dictionary[x] = dictionary[x] + 1

    number_set = set(dictionary.values())
    appears = [0, 0]

    if 2 in number_set:
        appears[0] = 1
    if 3 in number_set:
        appears[1] = 1

    return appears


def count_checksum(box_ids_list):
    twos = 0
    threes = 0

    for x in box_ids_list:
        result = count_letters_of_id(x)
        twos = twos + result[0]
        threes = threes + result[1]

    return twos * threes


def count_differences(my_list_1, my_list_2):
    differences = []
    for x in range(0, len(my_list_1)):
        if my_list_1[x] != my_list_2[x]:
            differences.append(my_list_1[x])
    if len(differences) == 1:
        return 1
    else:
        return 0


def find_correct_box_ids(box_ids_list):
    for i in range(0, len(box_ids_list)-1):
        for j in range (i+1, len(box_ids_list)):
            different_characters = count_differences(box_ids_list[i], box_ids_list[j])
            if different_characters == 1:
                ids = (i, j)
                break

    # we have indices of strings which differ by only one character
    # now I want to find common substring for these elements

    str_1 = box_ids_list[ids[0]]
    str_2 = box_ids_list[ids[1]]
    common_substring = ""
    for x in range(0, len(str_1)):
        if str_1[x] == str_2[x]:
            common_substring = common_substring + str_1[x]

    return common_substring


box_ids_list = get_input('2018/Day2/input.txt')
print("Checksum of box IDs (part 1): {}".format(count_checksum(box_ids_list)))
print("Common letter between the two correct box IDs (part 2): {}".format(find_correct_box_ids(box_ids_list)))

