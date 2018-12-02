from collections import Counter
import sys


def read(name):
    with open(name) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    data = read("day2input")
    twice = 0
    thrice = 0
    for line in data:
        counter = Counter(line)
        for letter in counter:
            if counter[letter] == 2:
                twice += 1
                break
        for letter in counter:
            if counter[letter] == 3:
                thrice += 1
                break
    print(twice * thrice)

    for linea in data:
        for lineb in data:
            if linea != lineb:
                difference = 0
                for a, b in zip(linea, lineb):
                    if a != b:
                        difference += 1
                        if difference >= 2:
                            break
                if difference == 1:
                    print("{} {}".format(linea, lineb))
                    sys.exit()
