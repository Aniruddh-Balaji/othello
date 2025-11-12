from tkinter import *

nb, nw, r = 2, 2, 1
d = {}
d1 = {}
d2 = {}


def welcome_screen():
    global welcome_window
    welcome_window = Tk(className="Othello", screenName="Othello")
    welcome_canvas = Canvas(welcome_window, bg="teal", width=6000, height=6000)
    welcome_window.geometry("50000x30000")
    welcome_canvas.place(x=0, y=0)
    welcome_label = Label(
        welcome_window,
        fg="lightpink",
        font=("Comic Sans", 40, "bold"),
        width=40,
        height=3,
        bg="teal",
        text="WELCOME TO OTHELLO!!!",
    )
    welcome_label.pack()
    start_button = Button(
        welcome_window,
        bg="pink",
        text="Begin",
        fg="teal",
        width=40,
        height=5,
        command=lambda: on_button_destroy1(welcome_window, win_player_names),
        font=300,
    )
    start_button.pack()


def win_player_names():
    global player1_name, player2_name
    win_player_names = Tk(className="Enter your names.")
    win_player_names.geometry("50000x30000")
    win_names_canvas = Canvas(win_player_names, bg="teal", width=15000, height=15000)
    win_names_canvas.place(x=0, y=0)
    player1_ask = Label(
        win_player_names, text="Player1", fg="black", bg="pink", font="bold", width=10
    )
    player2_ask = Label(
        win_player_names, text="Player2", fg="black", bg="pink", font="bold", width=10
    )
    player1_ask.place(x=500, y=177)
    player2_ask.place(x=800, y=177)
    player1_name = Entry(win_player_names, width=30)
    player2_name = Entry(win_player_names, width=30)
    player1_name.place(x=537, y=203)
    player2_name.place(x=837, y=203)
    start_button = Button(
        win_player_names,
        bg="pink",
        text="StartGame",
        fg="teal",
        width=40,
        height=5,
        command=lambda: on_button_destroy(win_player_names, starting_pos),
        font=40,
    )
    start_button.place(x=550, y=300)


def create_board():
    global s
    global d, d1
    global game_canvas
    global win_game
    global player1, player2
    win_game = Tk(className="Othello")
    win_game.geometry("50000x30000")
    game_canvas = Canvas(win_game, width=4000, height=6000, bg="teal")
    game_canvas.place(x=0, y=0)
    for i in range(64):
        h = i % 8
        w = i // 8
        game_canvas.create_rectangle(
            550 + 50 * h,
            100 + 50 * w,
            550 + 50 * (h + 1),
            100 + 50 * (w + 1),
            fill="darkgreen",
            outline="black",
            width=2,
        )
        d1[(h, w)] = (575 + 50 * w, 125 + 50 * h)
        d[(w, h)] = (550 + 50 * h, 100 + 50 * w, 550 + 50 * (h + 1), 100 + 50 * (w + 1))
    welcome_disp = Label(
        win_game, text="Welcome To Othello!!!", bg="lightpink", fg="black", font="bold"
    )
    welcome_disp.place(x=650, y=0)
    nb_pieces = Label(win_game, text=player1 + ": " + str(nb))
    nw_pieces = Label(win_game, text=player2 + ": " + str(nw))
    nb_pieces.place(x=650, y=30)
    nw_pieces.place(x=790, y=30)
    undo = Button(win_game, text="undo", fg="pink", bg="teal")
    undo.place(x=1, y=1)


def starting_pos():
    global d
    global d1
    global s
    s = {(2, 3), (3, 2), (4, 5), (5, 4)}
    create_board()
    put_coin(3, 3, 2, d)
    put_coin(3, 4, 1, d)
    put_coin(4, 4, 2, d)
    put_coin(4, 3, 1, d)
    check_val(s, d1)


def put_coin(i, j, r, d):
    global game_canvas
    global win_game
    x = d[(i, j)][0]
    y = d[(i, j)][1]
    z = d[(i, j)][2]
    a = d[(i, j)][3]
    if r == 2:
        game_canvas.create_oval(
            x + 4, y + 4, z - 4, a - 4, fill="white", outline="black", width=4
        )
    elif r == 1:
        game_canvas.create_oval(
            x + 4, y + 4, z - 4, a - 4, fill="black", outline="white", width=2
        )


def check_val(s, d1):
    global d2
    global win_game
    for i in s:
        d2[i] = Button(
            win_game,
            width=5,
            height=2,
            bg="lightgreen",
            command=lambda ci=i, rr=r: on_button_click(ci, rr),
        )
        d2[i].place(x=d1[i][0] - 20, y=d1[i][1] - 20)


def win_display(x):
    global win_game
    win_game.destroy()
    winner_display = Tk(className="Winner")
    if x == 1:
        Label(
            winner_display,
            text=player1 + " wins!!!",
            fg="lightpink",
            bg="teal",
            font=("Algerian", 40, "bold"),
            width=50,
            height=18,
        ).place(x=0, y=0)
    if x == 2:
        Label(
            winner_display,
            text=player2 + " wins!!!",
            fg="lightpink",
            bg="teal",
            font=("Times New Roman", 40, "bold"),
            width=50,
            height=18,
        ).place(x=0, y=0)


welcome_screen()


def on_button_click(i, r):
    for j in d2:
        d2[j].destroy()


def on_button_destroy(win1, win2):
    global player1, player2
    player1 = player1_name.get()
    player2 = player2_name.get()
    if player1 == "":
        player1 = "PLAYER1"
    if player2 == "":
        player2 = "PLAYER2"
    win1.destroy()
    win2()


def on_button_destroy1(win1, win2):
    win1.destroy()
    win2()


# win_display(1)


"""def undo(file):
    f=open(file,r)
    f.seek()
    f.readlines(8)"""


"""for i in range(8):
    for j in range(8):
        put_coin(i,j,l[i][j],d)"""
