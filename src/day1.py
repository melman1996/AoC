import sys


def read(name):
    with open(name) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    data = read("day1input")

    a = 0
    for line in data:
        if line[0] == "+":
            a += int(line[1:])
        elif line[0] == "-":
            a -= int(line[1:])
    print(a)

    a = 0
    freq = dict()
    for i in range(100000):
        for line in data:
            if line[0] == "+":
                a += int(line[1:])
            elif line[0] == "-":
                a -= int(line[1:])

            if a in freq:
                freq[a] += 1
                if freq[a] >= 2:
                    print("{} occured twice".format(a))
                    sys.exit()
            else:
                freq[a] = 1