def readsave():
    a = []
    with open("save.txt", "r") as file:
        lines = file.readlines()[2:12]
        a.append(int(lines[0].strip()))
        for line in lines[2:10]:
            l = line.strip()
            a.append(list(map(int, l.split())))
    return a


def writesave(l, c):
    with open("save.txt", "r") as file:
        lines = file.readlines()[0:4]

    lines[2] = str(c) + "\n"
    for i in l:
        s = " ".join(map(str, i)) + "\n"
        lines.append(s)

    with open("save.txt", "w") as file:
        file.writelines(lines)


def resetsave():
    l = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    writesave(l, 1)


# resetsave()
# print(*readsave(), sep='\n')
# writesave(readsave()[1:9], 1)
