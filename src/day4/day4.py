import re
import collections
import operator


def read(name):
    with open(name) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    data = read("day4input")
    dict = {}
    for line in data:
        dict["".join(re.findall('\d+', line)[0:5])] = line.split("]")[1][1:]

    dict = collections.OrderedDict(sorted(dict.items()))

    guards = {}
    guard_id = 0
    timestamp = 0
    for key in dict:
        if dict[key] == "falls asleep":
            timestamp = int(key[-2:])
        elif dict[key] == "wakes up":
            for i in range(timestamp, int(key[-2:])):
                guards[guard_id][i] += 1
        else:
            guard_id = re.findall('\d+', dict[key])[0]
            if guard_id not in guards:
                guards[guard_id] = [0] * 60

    max_id = guard_id
    for guard in guards:
        if sum(guards[guard]) > sum(guards[max_id]):
            max_id = guard

    print("{} {}".format(max_id, guards[max_id].index(max(guards[max_id]))))

    max_id = guard_id
    max_minute = 0
    for guard in guards:
        print("#{} {}".format(guard, guards[guard]))
        for minute in guards[guard]:
            if minute > max_minute:
                max_id = guard
                max_minute = minute

    print("{} {} {}".format(max_id, guards[max_id].index(max_minute), max_minute))
