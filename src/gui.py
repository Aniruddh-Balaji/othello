from tkinter import *
from game_logic import *
from board import *

root = None
win_names = None
win_game = None
game_canvas = None
d = {}
d1 = {}
d2 = {}

player1 = "PLAYER1"
player2 = "PLAYER2"
nb = 2
nw = 2

state = None
colour = 1
label_player1_count = None
label_player2_count = None
label_status = None


def welcome_screen():
    """Create root window with a Begin button."""
    global root
    root = Tk()
    root.title("Othello - Welcome")
    root.geometry("720x240")
    root.configure(bg="teal")

    Label(
        root,
        text="WELCOME TO OTHELLO!!!",
        fg="lightpink",
        bg="teal",
        font=("Comic Sans MS", 28, "bold"),
    ).pack(pady=10)

    Button(
        root,
        text="Begin",
        bg="pink",
        fg="teal",
        width=24,
        height=3,
        command=open_names_window,
    ).pack(pady=10)


def open_names_window():
    """Open the Tkinter to enter player names. Destroy welcome root."""
    global root, win_names
    if root:
        root.destroy()
        root = None

    win_names = Tk()
    win_names.title("Enter your names")
    win_names.geometry("420x180")
    win_names.configure(bg="teal")

    Label(win_names, text="Player 1:", bg="teal", fg="black").grid(
        row=0, column=0, padx=8, pady=8
    )
    Label(win_names, text="Player 2:", bg="teal", fg="black").grid(
        row=1, column=0, padx=8, pady=8
    )

    entry_p1 = Entry(win_names, width=30)
    entry_p2 = Entry(win_names, width=30)
    entry_p1.grid(row=0, column=1, padx=8, pady=8)
    entry_p2.grid(row=1, column=1, padx=8, pady=8)

    def start_game():
        p1 = entry_p1.get().strip()
        p2 = entry_p2.get().strip()
        global player1, player2
        player1 = p1 if p1 else "PLAYER1"
        player2 = p2 if p2 else "PLAYER2"
        win_names.destroy()
        initialize_game()

    Button(win_names, text="Start Game", bg="pink", fg="teal", command=start_game).grid(
        row=2, column=0, columnspan=2, pady=10
    )


def initialize_game():
    """Prepare game state from save, create board and show starting position."""
    global state, colour, win_game

    r = readsave()
    state = r[1:9]
    create_game_window()
    draw_full_board()
    update_counts()
    next_turn()


def create_game_window():
    """Create the TKinter game window and draw the grid. Fill d and d1 maps."""
    global win_game, game_canvas, d, d1, label_player1_count, label_player2_count, label_status

    win_game = Tk()
    win_game.title("Othello")
    win_game.geometry("420x600")
    win_game.configure(bg="teal")
    game_canvas = Canvas(win_game, width=420, height=520, bg="teal")
    game_canvas.place(x=0, y=0)
    d.clear()
    d1.clear()
    for i in range(64):
        h = i % 8
        w = i // 8
        x1 = 10 + 50 * h
        y1 = 40 + 50 * w
        x2 = 10 + 50 * (h + 1)
        y2 = 40 + 50 * (w + 1)
        game_canvas.create_rectangle(
            x1, y1, x2, y2, fill="darkgreen", outline="black", width=2
        )
        d[(w, h)] = (x1, y1, x2, y2)
        d1[(w, h)] = ((x1 + x2) // 2, (y1 + y2) // 2)
    Label(win_game, text="Welcome To Othello!!!", bg="lightpink", fg="black").place(
        x=10, y=470
    )

    label_player1_count = Label(
        win_game, text=f"{player1} :: {nb}", bg="teal", fg="black"
    )
    label_player1_count.place(x=10, y=500)
    label_player2_count = Label(
        win_game, text=f"{player2} :: {nw}", bg="teal", fg="black"
    )
    label_player2_count.place(x=200, y=500)

    label_status = Label(
        win_game, text="", bg="teal", fg="white", font=("Arial", 10, "bold")
    )
    label_status.place(x=10, y=525)


def draw_full_board():
    """Clear coins and draw coins according to global 'state'."""
    global game_canvas
    if game_canvas is None:
        return
    game_canvas.delete("all")
    for (w, h), (x1, y1, x2, y2) in d.items():
        game_canvas.create_rectangle(
            x1, y1, x2, y2, fill="darkgreen", outline="black", width=2
        )
    if state is None:
        return
    for i in range(8):
        for j in range(8):
            val = state[i][j]
            if val != 0:
                put_coin(i, j, val)


def put_coin(i, j, r):
    """Put a coin at board cell (i,j) with color r (1=black,2=white)."""
    global game_canvas, d
    x1, y1, x2, y2 = d[(i, j)]
    if r == 2:
        game_canvas.create_oval(
            x1 + 4, y1 + 4, x2 - 4, y2 - 4, fill="white", outline="black", width=4
        )
    elif r == 1:
        game_canvas.create_oval(
            x1 + 4, y1 + 4, x2 - 4, y2 - 4, fill="black", outline="white", width=2
        )


def update_counts():
    """Update the piece count labels using game_logic.count()."""
    global label_player1_count, label_player2_count, nb, nw, player1, player2
    c = count(state)
    nb, nw = c[0], c[1]
    if label_player1_count:
        label_player1_count.config(text=f"{player1} :: {nb}")
    if label_player2_count:
        label_player2_count.config(text=f"{player2} :: {nw}")


def clear_move_buttons():
    """Destroy any currently placed move buttons."""
    global d2
    for btn in list(d2.values()):
        btn.destroy()
    d2.clear()


def place_buttons(moves_set):
    """
    Place buttons on current valid moves (moves_set is a set of (i,j) tuples).
    The callbacks call on_move((i,j)).
    """
    global d1, d2, win_game
    clear_move_buttons()
    for pos in moves_set:
        cx, cy = d1[pos]
        b = Button(
            win_game,
            bg="lightgreen",
            command=lambda p=pos: on_move(p),
        )
        # place so button center roughly overlaps cell center
        b.place(x=cx - 23, y=cy - 23, width=45, height=45)
        d2[pos] = b


def on_move(pos):
    """
    Callback when a valid-move button is clicked.
    Apply move, save, switch colour, redraw and continue game.
    """
    global state, colour
    x, y = pos
    state = moves(state, colour, x, y)
    writesave(state, colour)
    colour = 3 - colour
    draw_full_board()
    update_counts()
    next_turn()


def next_turn():
    """
    Compute next legal moves and place buttons.
    Handle passes and game end.
    """
    global state, colour, label_status

    m = listmoves(state, colour)
    if len(m) == 0:
        other = 3 - colour
        m2 = listmoves(state, other)
        if len(m2) == 0:
            clear_move_buttons()
            update_counts()
            if nb > nw:
                result = f"{player1} wins! {nb} : {nw}"
            elif nw > nb:
                result = f"{player2} wins! {nw} : {nb}"
            else:
                result = f"Draw! {nb} : {nw}"
            if label_status:
                label_status.config(text=result)
            return
        else:

            if label_status:
                label_status.config(text=f"Player {colour} has no moves and must pass.")
            colour = other
            place_buttons(m2)
            return
    if label_status:
        label_status.config(text=f"{player1 if colour==1 else player2}'s turn.")
    place_buttons(m)


welcome_screen()
mainloop()
