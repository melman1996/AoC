import re
import sys


def read(name):
    with open(name) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


def do_overlap(a, b):#accepts [x, y, width, height]
    if a[0] > b[0] + b[2] or a[0] + a[2] < b[0]:
        return False
    if a[1] > b[1] + b[3] or a[1] + a[3] < b[1]:
        return False
    return True


if __name__ == "__main__":
    data = read("day3input")
    matrix = [[0 for i in range(1000)] for i in range(1000)]
    data = [list(map(int, re.findall('\d+', line))) for line in data]
    for line in data:
        for i in range(line[3]):
            for j in range(line[4]):
                matrix[line[1] + i][line[2] + j] += 1
    counter = 0
    for line in matrix:
        for x in line:
            if x > 1:
                counter += 1
    print(counter)


    for linea in data:
        overlap = False
        for lineb in data:
            if linea != lineb and do_overlap(linea[1:], lineb[1:]):
                overlap = True
                break
        if not overlap:
            print(linea[0])
            sys.exit()
