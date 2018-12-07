


def read(name):
    with open(name) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    size = 400
    data = read("day6input")
    data = [list(map(int, line.split(", "))) for line in data]
    grid = [["-"] * size for i in range(size)]

    for i in range(len(data)):
        grid[data[i][0]][data[i][1]] = str(i)

    for distance in range(1, size):
        for i in range(len(data)):
            for x in range(-distance, distance + 1):
                y = distance - abs(x)
                coord = (data[i][0] + x, data[i][1] + y)
                if coord[0] >= 0 and coord[0] < size and coord[1] >= 0 and coord[1] < size:
                    if grid[coord[0]][coord[1]] == "-":
                        grid[coord[0]][coord[1]] = str(i) + "t"
                    elif grid[coord[0]][coord[1]].endswith("t"):
                        grid[coord[0]][coord[1]] = "."
                if y != 0:
                    coord = (data[i][0] + x, data[i][1] - y)
                    if coord[0] >= 0 and coord[0] < size and coord[1] >= 0 and coord[1] < size:
                        if grid[coord[0]][coord[1]] == "-":
                            grid[coord[0]][coord[1]] = str(i) + "t"
                        elif grid[coord[0]][coord[1]].endswith("t"):
                            grid[coord[0]][coord[1]] = "."
        for q in range(len(grid)):
            for w in range(len(grid[q])):
                if grid[q][w].endswith("t"):
                    grid[q][w] = grid[q][w][0]


    stats = [0] * len(data)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                stats[int(grid[i][j])] += 1
            except Exception:
                pass
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                try:
                    stats[int([grid[i][j]])] = 0
                except Exception:
                    pass
    print(max(stats))
