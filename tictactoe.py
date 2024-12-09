from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLable1 = Label(frame1, text="Tic Tac Toe", font= "Arial, 30")
titleLable1.pack()

frame2 = Frame(root)
frame2.pack()

turn = "X"

game_end = False

board = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

def play(event):
    global turn, game_end

    if game_end:
        return

    button = event.widget
    buttontext = str(button)
    clicked = buttontext[-1]

    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " " and turn == "X":  # Only allow X to play during their turn
        button["text"] = "X"
        board[clicked] = "X"

        # Check if X wins
        if winner("X"):
            winnerlabel = Label(frame2, text="X wins the game!", font="Arial, 22", bg="yellow")
            winnerlabel.grid(row=4, column=0, columnspan=3)
            game_end = True
            return

        # Check if it's a draw
        if isDraw(board):
            winnerlabel = Label(frame2, text="It is a Draw!!", font="Arial, 22", bg="yellow")
            winnerlabel.grid(row=4, column=0, columnspan=3)
            game_end = True
            return

        # Switch turn to O and let the computer play
        turn = "O"
        playComputer()

def playComputer():
    global board, game_end, turn

    if game_end:
        return

    # Check for immediate winning moves for "O"
    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            if winner("O"):
                buttons[key - 1]["text"] = "O"
                winnerlabel = Label(frame2, text="O wins the game!", font="Arial, 22", bg="yellow")
                winnerlabel.grid(row=4, column=0, columnspan=3)
                game_end = True
                return
            board[key] = " "  # Undo move

    # Check for immediate blocking moves to prevent "X" from winning
    for key in board.keys():
        if board[key] == " ":
            board[key] = "X"
            if winner("X"):
                board[key] = "O"  # Block "X"
                buttons[key - 1]["text"] = "O"
                turn = "X"  # Switch turn back to X
                return
            board[key] = " "  # Undo move

    # Use minimax to determine the best move
    best_score = -float('inf')
    best_move = None

    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            score = minimax(board, False)
            board[key] = " "  # Undo move
            if score > best_score:
                best_score = score
                best_move = key

    # Make the best move
    if best_move is not None:
        board[best_move] = "O"
        buttons[best_move - 1]["text"] = "O"

    # Check for a draw
    if isDraw(board):
        winnerlabel = Label(frame2, text="It is a Draw!!", font="Arial, 22", bg="yellow")
        winnerlabel.grid(row=4, column=0, columnspan=3)
        game_end = True
        return

    # Switch turn back to X
    turn = "X"

def minimax(board, isMaximizing):
    # Check terminal states
    if winner("X"):
        return -1  # "X" wins
    if winner("O"):
        return 1   # "O" wins
    if isDraw(board):
        return 0   # Draw

    if isMaximizing:  # Maximizing for "O"
        best_score = -float('inf')
        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                score = minimax(board, False)
                board[key] = " "  # Undo move
                best_score = max(best_score, score)
        return best_score
    else:  # Minimizing for "X"
        best_score = float('inf')
        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                score = minimax(board, True)
                board[key] = " "  # Undo move
                best_score = min(best_score, score)
        return best_score

def isDraw(board):
    return all(value != " " for value in board.values()) and winner("X") is None and winner("O") is None

def winner(player):
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return player
    return None

button1 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button1.grid(row= 0, column= 0)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button2.grid(row= 0, column= 1)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button3.grid(row= 0, column= 2)
button3.bind("<Button-1>", play)

button4 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button4.grid(row= 1, column= 0)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button5.grid(row= 1, column= 1)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button6.grid(row= 1, column= 2)
button6.bind("<Button-1>", play)

button7 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button7.grid(row= 2, column= 0)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button8.grid(row= 2, column= 1)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text = " ", height = 2, width = 4, font = "Arial, 21", relief = RAISED, borderwidth = 5)
button9.grid(row= 2, column= 2)
button9.bind("<Button-1>", play)

def restart(event):
    global board, game_end, turn, buttons
    game_end = False
    turn = "X"  # Reset turn to default
    board = {i: " " for i in range(1, 10)}
    for button in buttons:
        button["text"] = " "
    winnerlabel = Label(frame2, text=" ", font="Arial, 22", width=13)
    winnerlabel.grid(row=4, column=0, columnspan=3)


buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

restart_button = Button(frame2, text = "Restart game", height = 1, width = 12)
restart_button.grid(row = 3, column = 0, columnspan = 3)
restart_button.bind("<Button-1>", restart)

root.mainloop()