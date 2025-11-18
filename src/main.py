from game_logic import *
from board import *

print()

if sum(count(readsave()[1:10])) == 64:
    resetsave()
else:
    s = input("Retrieve previous game(y/n)? ")
    if s.lower() == "n":
        resetsave()

state = readsave()[1:10]
colour = readsave()[0]

code = 1
while code:
    print()
    print(colour, "to play")
    print(*state, sep="\n")
    print()
    m = listmoves(state, colour)
    if len(m) == 0:
        print("No moves left, switching player")
        colour = 3 - colour
        if len(listmoves(state, colour)) == 0:
            print("No moves left")
            code = 0
            break
    else:
        print("Valid moves:", *sorted(list(m)))
        x, y = map(int, input("Enter valid x, y values: ").split())
        if (x, y) in m:
            state = moves(state, colour, x, y)
            colour = 3 - colour
            writesave(state, colour)
