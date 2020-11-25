import tkinter as tk
from tkinter import messagebox

from ticktacktoe import grid, ai


class App:
    main_window = None
    grid = None
    ai = None
    button_ids = []
    player_done = False

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Tick Tack Toe")
        self.grid = grid.Grid()
        self.init_buttons(self.main_window)
        self.ai = ai.AI()

    def init_buttons(self, window):
        for i in range(self.grid.N):
            for j in range(self.grid.N):
                btn = tk.Button(window, text=" ", font=("Arial Bold", 50), height=2, width=5)
                btn.tag = repr(i) + repr(j)
                btn.grid(row=i, column=j)
                btn.bind("<ButtonPress-1>", self.on_click)
                btn.bind("<ButtonRelease-1>", self.on_release)
                self.button_ids.append(btn)

    def start(self):
        self.main_window.mainloop()

    def on_click(self, event):
        if self.player_done:
            return
        obj = event.widget
        (i, j) = divmod(int(obj.tag), 10)
        if self.grid.field[i][j] != 0:
            return
        obj.config(text="X")
        self.grid.mark(i, j)
        self.player_done = True

    def on_release(self):
        if not self.player_done:
            return
        self.check_grid()
        self.ai_turn()
        self.player_done = False
        self.check_grid()

    def check_grid(self):
        if self.grid.check() == 1:
            self.player_wins()
        elif self.grid.check() == -1:
            self.player_loose()

    def ai_turn(self):
        (i, j) = ai.AI.mark_cell(self.ai, self.grid)
        if i is None and j is None:
            self.nobody_wins()
        self.button_ids[i * self.grid.N + j].config(text="O")
        self.grid.mark(i, j, -1)

    def player_wins(self):
        messagebox.showinfo("You win!", "You win!")
        self.main_window.destroy()

    def nobody_wins(self):
        messagebox.showinfo("Nobody wins!", "Nobody wins!")
        self.main_window.destroy()

    def player_loose(self):
        messagebox.showinfo("You loose!", "You loose!")
        self.main_window.destroy()


if __name__ == "__main__":
    app = App()
    app.start()
