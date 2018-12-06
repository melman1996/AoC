


def read(name):
    with open(name) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    original = read("day5input")[0]
    # while True:
    #     length = len(data)
    #     for i in range(len(data) - 1):
    #         difference = ord(data[i]) - ord(data[i + 1])
    #         if abs(difference) == 32:
    #             data = data[:i] + data[i + 2:]
    #             break
    #     if length == len(data):
    #         print(len(data))
    #         break
    for i in range(ord('Z'), ord('Z') + 2):
        data = original
        data = data.replace(chr(i), "")
        data = data.replace(chr(i + 32), "")
        while True:
            length = len(data)
            for j in range(len(data) - 1):
                difference = ord(data[j]) - ord(data[j + 1])
                if abs(difference) == 32:
                    data = data[:j] + data[j + 2:]
                    break
            if length == len(data):
                print("Removed {}/{}: {}".format(chr(i), chr(i + 32), len(data)))
                break
