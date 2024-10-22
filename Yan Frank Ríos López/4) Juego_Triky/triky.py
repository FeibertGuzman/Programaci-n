from tkinter import *
import random 

def next_turn(row, column):

    global  player

    if buttons[row][column]["text"] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text="Turno para " + players[1])
            elif check_winner() is True:
                label.config(text="Ganó " + players[0])
            elif check_winner() == "Empate":
                label.config(text="¡Empate!")
        else:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text="Turno para " + players[0])
            elif check_winner() is True:
                label.config(text="Ganó " + players[1])
            elif check_winner() == "Empate":
                label.config(text="¡Empate!")
    

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
           buttons[row][0].config(bg="green")
           buttons[row][1].config(bg="green")
           buttons[row][2].config(bg="green")
           return True
        
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
           buttons[0][column].config(bg="green")
           buttons[1][column].config(bg="green")
           buttons[2][column].config(bg="green")
           return True
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range (3):
                buttons[row][column].config(bg="red")
        return "Empate"
    else:
        return False

def empty_spaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
              if buttons[row][column]["text"] != "":
                  spaces -= 1
                  
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    
    global player

    player = random.choice(players)

    label.config(text="Turno para " + player)

    for row in range(3):
        for column in range (3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Triky")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0], 
           [0,0,0],
           [0,0,0]]

label = Label(text="Turno para " + player, font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="Reinciar", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consola", 40), width=5, height=2, command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()