import tkinter as tk

class GUI:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        # TODO

    def set_controller(self, controller):
        self.controller = controller
        # TODO

    def begin(self):
        self.root.mainloop()