def readsave():
    """
    Reads the text file `save.txt` and returns the state
    """
    a = []
    with open("save.txt", "r") as file:
        lines = file.readlines()[2:12]
        a.append(int(lines[0].strip()))
        for line in lines[2:10]:
            state = line.strip()
            a.append(list(map(int, state.split())))
    return a


def writesave(state, color):
    """
    Overwrites the `state` to `save.txt`
    """
    with open("save.txt", "r") as file:
        lines = file.readlines()[0:4]

    lines[2] = str(color) + "\n"
    for i in state:
        s = " ".join(map(str, i)) + "\n"
        lines.append(s)

    with open("save.txt", "w") as file:
        file.writelines(lines)


def resetsave():
    """
    Initializes the state.
    """
    state = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    writesave(state, 1)
