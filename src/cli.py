from game_logic import *
from board import *

print("\nWELCOME TO OTHELLO\n")

if sum(count(readsave()[1:10])) == 64:
    print("\nPrevious game ended, starting new game\n")
    resetsave()
else:
    s = input("[1] Start new game\n[2] Load previous game\n[3] Quit\nOption: ")
    if s == '1':
        resetsave()
    elif s != '2':
        exit()

state = readsave()[1:10]
colour = readsave()[0]

code = 1
while code:
    print()
    print(colour, "to play\n")
    for i in state:
        print(*i)
    print()
    m = listmoves(state, colour)
    if len(m) == 0:
        print("\nNo moves left, switching player")
        colour = 3 - colour
        if len(listmoves(state, colour)) == 0:
            print("No moves left")
            code = 0
            break
    else:
        print("Valid moves:", *sorted(list(m)))
        s = input("Your move\nx y: ").split()
        try:
            x, y = map(int, s)
            if (x, y) in m:
                state = moves(state, colour, x, y)
                colour = 3 - colour
                writesave(state, colour)
            else:
                print("\nInvalid move, try again")

        except:
            print("\nInvalid input")
            op = input("[1] try again\n[2] quit\nOption: ")
            if op == '2':
                break

print("\nFinal Scores\nPlayer 1:", count(state)[0], "\nPlayer 2:", count(state)[1])

if code == 0:
    if count(state)[0] > count(state)[1]:
        print("\nPlayer 1 wins!")
    elif count(state)[1] > count(state)[0]:
        print("\nPlayer 2 wins!")
    else:
        print("\nDraw")

print("\nOk friend, bye")
