import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="lightblue")

buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"

def reset_board():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"
            buttons[i][j].configure(bg="white", fg="black")

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return buttons[row][0]["text"]
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return buttons[0][col]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]
    return None

def check_tie():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True

def on_button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col].configure(fg="blue" if current_player == "X" else "red")
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        elif check_tie():
            messagebox.showinfo("Tic Tac Toe", "The game is a tie!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

header = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="lightblue")
header.grid(row=0, column=0, columnspan=3, sticky="nsew")

for i in range(3):
    root.grid_rowconfigure(i+1, weight=1)
    for j in range(3):
        root.grid_columnconfigure(j, weight=1)
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), bg="white", command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

root.grid_rowconfigure(4, weight=1)
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), bg="lightgrey", command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)

root.mainloop()
