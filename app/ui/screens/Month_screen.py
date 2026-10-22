import tkinter as tk

class MonthScreen:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#101820")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(self.frame, text="Month", fg="#fffff0", bg="#101820")
        title.pack(pady=20)
        label = tk.Label(self.frame, text="This is the Month screen.", fg="#fffff0", bg="#101820")
        label.pack(pady=10)





    
    #region show/hide methods
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()
    #endregion show/hide methods