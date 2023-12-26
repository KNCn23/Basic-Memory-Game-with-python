import tkinter as tk
from random import shuffle
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        root.title("Memory Game")

        # Game variables
        self.buttons = {}
        self.first_selection = None
        # 10 pairs for a 4x5 grid (total 20 elements)
        self.pairs = list(range(1, 11)) * 2
        shuffle(self.pairs)

        # Set up the game board
        for i in range(20): # Creating a 4x5 grid
            button = tk.Button(root, text="MG", width=10, height=5,
                               command=lambda i=i: self.on_button_press(i))
            button.grid(row=i // 5, column=i % 5)
            self.buttons[i] = button

    def on_button_press(self, i):
        if self.first_selection is None:
            self.first_selection = i
            self.buttons[i].config(text=str(self.pairs[i]))
            self.root.update_idletasks()
        else:
            if self.first_selection != i: # Check if the same button is not clicked twice
                self.buttons[i].config(text=str(self.pairs[i]))
                self.root.update_idletasks()
                # Check for match
                if self.pairs[i] == self.pairs[self.first_selection]:
                    self.buttons[i].config(state="disabled")
                    self.buttons[self.first_selection].config(state="disabled")
                else:
                    # No match, reset after a short delay
                    self.root.after(500, self.hide_buttons, i, self.first_selection)
                self.first_selection = None

    def hide_buttons(self, i, j):
        self.buttons[i].config(text="MG")
        self.buttons[j].config(text="MG")

# Create the main window
root = tk.Tk()
game = MemoryGame(root)
root.mainloop()
