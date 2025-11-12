def rowcheck(row, color):
    """
    Takes a list `r` and `color` and returns indices of valid moves in that list.
    """
    # x is the index of the first useful 0 encountered
    # y is the index of the first color coin encountered
    # -1 => not found
    x = y = -1
    code = 0  # Positive if the other color is encountered
    ans = []  # The list of valid moves
    for i in range(len(row)):
        if row[i] == 0:
            x = i
            if not code:
                y = -1
            elif y != -1:
                ans.append(x)
                y = -1
            code = 0
        elif row[i] == color:
            y = i
            if not code:
                x = -1
            elif x != -1:
                ans.append(x)
                x = -1
            code = 0
        else:
            code += 1
    return ans


def listmoves(state, color):
    """
    Outputs the coordinates of all valid moves, given the current state `state` and `color`
    """
    valid_moves = set()

    # Checks all Rows and Columns
    for i in range(8):
        a = rowcheck(state[i], color)
        for j in a:
            valid_moves.add((i, j))
        x = []
        for j in range(8):
            x.append(state[j][i])
        a = rowcheck(x, color)
        for j in a:
            valid_moves.add((j, i))

    # Checks diagonals with length greater than 2
    # This checks the top left and bottom left triangles
    for j in range(6):
        x = []
        for i in range(0, 8 - j):
            x.append(state[i][j + i])
        a = rowcheck(x, color)
        for i in a:
            valid_moves.add((i, j + i))
        y = []
        for i in range(7, j - 1, -1):
            y.append(state[i][7 - i + j])
        a = rowcheck(y, color)
        for i in a:
            valid_moves.add((7 - i, i + j))

    # Checks diagonals with length greater than 2
    # This checks the top right and bottom right triangles
    for j in range(2, 8):
        x = []
        for i in range(0, j + 1):
            x.append(state[i][j - i])
        a = rowcheck(x, color)
        for i in a:
            valid_moves.add((i, j - i))
        y = []
        for i in range(7, 6 - j, -1):
            y.append(state[i][i + j - 7])
        a = rowcheck(y, color)
        for i in a:
            valid_moves.add((7 - i, j - i))

    return valid_moves


def rowmove(row, color, j):
    """
    Returns the operations on `row` with index `j` for `color` that needs to take place.
    """
    ans = []

    # a consists of all indices left of `j` which have to be set to `color`
    a = [j]
    code = 0
    for i in range(j - 1, -1, -1):
        if row[i] == 3 - color:
            code = 1
            a.append(i)
        elif row[i] == color and code:
            code = 2
            break
        else:
            code = 0
            break
    if code == 2:
        ans += a

    # b consists of all indices right of `j` which have to be set to `color`
    b = [j]
    code = 0
    for i in range(j + 1, len(row)):
        if row[i] == 3 - color:
            code = 1
            b.append(i)
        elif row[i] == color and code:
            code = 2
            break
        else:
            code = 0
            break
    if code == 2:
        return ans + b
    else:
        return ans


def moves(state, color, x, y):
    """
    Given `x`, `y` coordinates and `color` along with `state`, it returns the modified board.
    """

    # For (x, y), we rowmove on the row of x(r1) the column of y(r2), primary diagonal(r3) and secondary diagonal(r4).

    r1 = rowmove(state[x], color, y)
    for j in r1:
        state[x][j] = color

    a = []  # Literally the column
    for i in range(8):
        a.append(state[i][y])
    r2 = rowmove(a, color, x)
    for i in r2:
        state[i][y] = color

    # The values of the diagonal elements
    d1 = [state[i][i - x + y] for i in range(8) if i - x + y in range(8)]
    # The coordinates of the diagonal elements
    d1c = [[i, i - x + y] for i in range(8) if i - x + y in range(8)]
    r3 = rowmove(d1, color, d1c.index([x, y]))
    for i in r3:
        state[d1c[i][0]][d1c[i][1]] = color

    # The values of the diagonal elements
    d2 = [state[i][x + y - i] for i in range(8) if x + y - i in range(8)]
    # The coordinates of the diagonal elements
    d2c = [[i, x + y - i] for i in range(8) if x + y - i in range(8)]
    r4 = rowmove(d2, color, d2c.index([x, y]))
    for i in r4:
        state[d2c[i][0]][d2c[i][1]] = color

    return state


def count(state):
    """
    Returns the count of white and black pieces, given a `state`
    """
    ans = [0, 0]
    for i in state:
        for j in i:
            if j:
                ans[j - 1] += 1
    return ans
