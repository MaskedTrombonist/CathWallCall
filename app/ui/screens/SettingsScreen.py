import tkinter as tk
from ui.colors import background_color, foreground_color

class SettingsScreen:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg=background_color)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()

    def create_widgets(self):
        self.label = tk.Label(self.frame, text="Settings", font=("DejaVu Sans", 20, "bold"), fg=foreground_color, bg=background_color)
        self.label.pack(pady=20)