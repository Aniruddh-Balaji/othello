def rowcheck(r, c):
    x = y = -1
    code = 0
    ans = []
    for i in range(len(r)):
        if r[i] == 0:
            x = i
            if not code:
                y = -1
            elif y != -1:
                ans.append(x)
                y = -1
            code = 0
        elif r[i] == c:
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


def listmoves(l, c):
    v = set()

    for i in range(8):
        a = rowcheck(l[i], c)
        for j in a:
            v.add((i, j))
        x = []
        for j in range(8):
            x.append(l[j][i])
        a = rowcheck(x, c)
        for j in a:
            v.add((j, i))

    for j in range(6):
        x = []
        for i in range(0, 8 - j):
            x.append(l[i][j + i])
        a = rowcheck(x, c)
        for i in a:
            v.add((i, j + i))
        y = []
        for i in range(7, j - 1, -1):
            y.append(l[i][7 - i + j])
        a = rowcheck(y, c)
        for i in a:
            v.add((7 - i, i + j))

    for j in range(2, 8):
        x = []
        for i in range(0, j + 1):
            x.append(l[i][j - i])
        a = rowcheck(x, c)
        for i in a:
            v.add((i, j - i))
        y = []
        for i in range(7, 6 - j, -1):
            y.append(l[i][i + j - 7])
        a = rowcheck(y, c)
        for i in a:
            v.add((7 - i, j - i))

    return v


def rowmove(r, c, j):
    ans = []

    a = [j]
    code = 0
    for i in range(j - 1, -1, -1):
        if r[i] == 3 - c:
            code = 1
            a.append(i)
        elif r[i] == c and code:
            code = 2
            break
        else:
            code = 0
            break
    if code == 2:
        ans += a

    b = [j]
    code = 0
    for i in range(j + 1, len(r)):
        if r[i] == 3 - c:
            code = 1
            b.append(i)
        elif r[i] == c and code:
            code = 2
            break
        else:
            code = 0
            break
    if code == 2:
        return ans + b
    else:
        return ans


def moves(l, c, x, y):
    r1 = rowmove(l[x], c, y)
    for j in r1:
        l[x][j] = c

    a = []
    for i in range(8):
        a.append(l[i][y])
    r2 = rowmove(a, c, x)
    for i in r2:
        l[i][y] = c

    d1 = [l[i][i - x + y] for i in range(8) if i - x + y in range(8)]
    d1c = [[i, i - x + y] for i in range(8) if i - x + y in range(8)]
    r3 = rowmove(d1, c, d1c.index([x, y]))
    for i in r3:
        l[d1c[i][0]][d1c[i][1]] = c

    d2 = [l[i][x + y - i] for i in range(8) if x + y - i in range(8)]
    d2c = [[i, x + y - i] for i in range(8) if x + y - i in range(8)]
    r4 = rowmove(d2, c, d2c.index([x, y]))
    for i in r4:
        l[d2c[i][0]][d2c[i][1]] = c
    return l


def count(l):
    ans = [0, 0]
    for i in l:
        for j in i:
            if j:
                ans[j - 1] += 1
    return ans
