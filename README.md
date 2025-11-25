<h1><center>Othello</center></h1>
An implementation of the famous board game Othello in python, using TKinter.

This is a first year college project and hence is not excellent, but it works and has all necessary functionality.

# How to install

Pre-requisites:
`git` must be installed and working on your system.
The python modules necessary is just TKinter. This is usually pre-packaged with Python.
In case it is not, you can run the following on Ubuntu/Debian-based systems:
```sh
$ sudo apt-get install python3-tk
```

Clone the repository,
```sh
$ git clone https://github.com/Aniruddh-Balaji/othello.git
```

# How to use
The rules of the board game Othello are concisely explained [here](https://www.wikihow.com/Play-Othello).

Running the program:
```sh
$ cd othello/src
$ python3 main.py
```

For GUI, 

When you run the program, you get the initial _Welcome_ screen, following which you get a window to input
your players' names into. If left empty, it is represented as `Player 1` and `Player 2`. We then get the game window.

Black begins, all possible squares for black are highlighted as buttons on the board. The black player should
click on one of the buttons; a black coin will be placed there and all necessary coin flips will be made.

This works similarly for white.

For CLI,

You get a nice printed board, with options to choose the next move as coordinates.
You should type out the coordinates and the game shall continue.

# Architecture
The architecture of the code is neatly mentioned [here](./ARCHITECTURE.md).

# Credits
The five members of the team are:
- [@roomroofroot](https://github.com/roomroofroot)
- [@kajuburfi](https://github.com/kajuburfi)
- [@aniruddh-balaji](https://github.com/Aniruddh-Balaji)
- [@the-deepak-nayak](https://github.com/the-deepak-nayak)
- [@devbrat-singh64](https://github.com/devbrat-singh64)

# License
The license for this program is a _slightly_ modified [MIT license](./LICENSE)
