import tkinter as tk
import math

root = tk.Tk()
root.title("AI Tic-Tac-Toe Game by Harshini")

board = [" "] * 9
buttons = []

def winning_conditions(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def box_is_full():
    return all(s != " " for s in board)

def minimax(board_state, depth, is_maximizing):
    if winning_conditions("O"):
        return 1
    if winning_conditions("X"):
        return -1
    if box_is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "O"
                score = minimax(board_state, depth+1, False)
                board_state[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "X"
                score = minimax(board_state, depth+1, True)
                board_state[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"
        buttons[move].config(text="O", state="disabled")

        if winning_conditions("O"):
            end_game("AI wins!")
        elif box_is_full():
            end_game("It's a draw!")

#Flow of the game
def clicked(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        if winning_conditions("X"):
            end_game("You win!")
        elif box_is_full():
            end_game("It's a draw!")
        else:
            ai_move()

def end_game(message):
    for b in buttons:
        b.config(state="disabled")
    result_label.config(text=message)

def restart_game():
    global board
    board = [" "] * 9
    for b in buttons:
        b.config(text="", state="normal", bg="lightyellow")
    result_label.config(text="")    

#Decorationss
for i in range(9):
    button = tk.Button(root, width=8, height=4, font=("Baguet Script", 16, "bold"),
                       bg="lightyellow", fg="black",
                       command=lambda i=i: clicked(i))
    button.grid(row=i//3, column=i%3, padx= 5, pady=5)
    buttons.append(button)

result_label = tk.Label(root, text="", font=("Baguet Script", 14, "bold"),
                        fg="green")
result_label.grid(row=3, column=0, columnspan=3)
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 12, "bold"),
                           bg="lightblue", command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
