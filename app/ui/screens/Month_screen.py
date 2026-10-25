import tkinter as tk
from ui.colors import background_color, foreground_color

class MonthScreen:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg=background_color)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(self.frame, text="Month", fg=foreground_color, bg=background_color)
        title.pack(pady=20)
        label = tk.Label(self.frame, text="This is the Month screen.", fg=foreground_color, bg=background_color)
        label.pack(pady=10)





    
    #region show/hide methods
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()
    #endregion show/hide methods