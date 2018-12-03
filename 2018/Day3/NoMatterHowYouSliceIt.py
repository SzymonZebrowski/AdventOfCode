def get_input(filename):
    rects = []
    #id @ x,y: w,h

    with open(filename) as file:
        for line in file:
            line = line[:-1]
            elements = line.split(" ")
            id = int(elements[0][1:])
            buf = elements[2].split(",")
            xy = (int(buf[0]), int(buf[1][:-1]))
            buf = elements[3].split("x")
            wh = (int(buf[0]), int(buf[1]))
            rects.append((id, xy, wh))

    return rects


def create_material():
    #material is a square
    material = [['.' for x in range(0, 1000)] for y in range(0, 1000)]

    return material


def fill_material(material, my_list):
    how_many_inches = 0
    for element in my_list:
        xy = element[1]
        wh = element[2]
        x = int(xy[0])
        y = int(xy[1])
        w = int(wh[0])
        h = int(wh[1])
        for i in range(x, x + w):
            for j in range(y, y+h):
                if material[i][j] == '.':
                    material[i][j] = '#'
                elif material[i][j] == '#':
                    material[i][j] = 'X'
                    how_many_inches = how_many_inches + 1

    return how_many_inches


def find_not_overlapping(material, my_list):
    id = None
    for element in my_list:
        xy = element[1]
        wh = element[2]
        x = int(xy[0])
        y = int(xy[1])
        w = int(wh[0])
        h = int(wh[1])
        elements_of_square = set([])
        for i in range(x, x + w):
            for j in range(y, y + h):
                elements_of_square.add(material[i][j])
        if 'X' not in elements_of_square:
            id = element[0]
            break

    return id


my_input = get_input("2018/Day3/input.txt")
material = create_material()
how_many_inches_common = fill_material(material, my_input)
id = find_not_overlapping(material, my_input)
print("Number of inches common (part 1): {}".format(how_many_inches_common))
print("Not overlapping id (part 2): {}".format(id))
