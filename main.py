import tkinter as tk
from tkinter import *
import random



# def next_turn(row, column): Nächsten Klick (Zug)
# Accsses to our player
# when the button is empty and there is yet no winner
# If the player is 'x' then put this player
# Then check if there is a winner after this input
# If not, change the text with the configuration 'config' and we switch players (The second player plays)
# We have 3 cases: a. check_winner() is False, b. check_winner() is True, c. check_winner() == 'Tie'
def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == 'Tie':
                label.config(text=("Tie"))
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == 'Tie':
                label.config(text=("Tie"))


# def check_winner()
# If the 3 rows or 3 columns are equal and != 0, then return true
# If the fields in one of the both diagonals are equal and != 0, then return true
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")

window = tk.Tk()
window.title('TicTacToe')
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = tk.Label(text=player + " turn", font=("consolas", 40))
label.pack(side="top")

reset_button = tk.Button(text="Restart", font=("consolas", 40), bg= "blue", command=new_game)
reset_button.pack(side="top")
frame = tk.Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 20), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
