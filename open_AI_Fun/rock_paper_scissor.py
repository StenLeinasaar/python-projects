import random
import tkinter as tk
from tkinter import messagebox


class RockPaperScissor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissor")
        self.geometry("300x300")
        self.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0

        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()

        self.player_choice.set("")
        self.computer_choice.set("")

        self.player_score_label = tk.Label(self, text="Player Score: {}".format(self.player_score))
        self.computer_score_label = tk.Label(self, text="Computer Score: {}".format(self.computer_score))

        self.player_choice_label = tk.Label(self, text="Player Choice: {}".format(self.player_choice.get()))
        self.computer_choice_label = tk.Label(self, text="Computer Choice: {}".format(self.computer_choice.get()))

        self.rock_button = tk.Button(self, text="Rock", command=lambda: self.play("rock"))
        self.paper_button = tk.Button(self, text="Paper", command=lambda: self.play("paper"))
        self.scissor_button = tk.Button(self, text="Scissor", command=lambda: self.play("scissor"))

        self.player_score_label.pack()
        self.computer_score_label.pack()

        self.player_choice_label.pack()
        self.computer_choice_label.pack()

        self.rock_button.pack()
        self.paper_button.pack()
        self.scissor_button.pack()

    def play(self, player):
        computer = random.choice(["rock", "paper", "scissor"])

        if player == computer:
            messagebox.showinfo("Tie", "It's a tie!")
        elif player == "rock":
            if computer == "paper":
                messagebox.showinfo("Lose", "You lose!")
                self.computer_score += 1
            else:
                messagebox.showinfo("Win", "You win!")
                self.player_score += 1
        elif player == "paper":
            if computer == "scissor":
                messagebox.showinfo("Lose", "You lose!")
                self.computer_score += 1
            else:
                messagebox.showinfo("Win", "You win!")
                self.player_score += 1
        elif player == "scissor":
            if computer == "rock":
                messagebox.showinfo("Lose", "You lose!")
                self.computer_score += 1
            else:
                messagebox.showinfo("Win", "You win!")
                self.player_score += 1

        self.player_choice.set(player)
        self.computer_choice.set(computer)

        self.player_score_label["text"] = "Player Score: {}".format(self.player_score)
        self.computer_score_label["text"] = "Computer Score: {}".format(self.computer_score)

        self.player_choice_label["text"] = "Player Choice: {}".format(self.player_choice.get())
        self.computer_choice_label["text"] = "Computer Choice: {}".format(self.computer_choice.get())


if __name__ == '__main__':
    game = RockPaperScissor()
    game.mainloop()