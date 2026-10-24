# TODO: Implement the TodayScreen UI with event buttons for today's events. using the create_event_button function from repeated_elements/event_button.py

import tkinter as tk
from tkinter import font
from datetime import datetime, timedelta
from ui.repeated_elements.event_button import create_event_button

class TodayScreen:
    def __init__(self, parent, calendar_service):
        self.calendar_service = calendar_service
        self.frame = tk.Frame(parent, bg="#101820")
        self.frame.pack(fill=tk.BOTH, expand=True)

        #region Frames

        #region title frames
        self.title_font = font.Font(family="DejaVu Sans", size=50, weight="bold")

        self.top_frame = tk.Frame(self.frame, bg="#101820")
        self.top_frame.pack(side=tk.TOP, fill=tk.X, expand=False)
        label = tk.Label(
            self.top_frame, 
            text="Today", 
            fg="#fffff0", 
            bg="#101820",
            font=self.title_font
            )
        label.pack(pady=20)
        self.top_line = tk.Frame(self.top_frame, bg="#fffff0", height=2)
        self.top_line.pack(fill=tk.X, padx=20, pady=(0, 20))

        #endregion title frame

        self.right_frame = tk.Frame(self.frame, bg="#101820")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.middle_line = tk.Frame(self.frame, bg="#fffff0", width=2)
        self.middle_line.pack(side=tk.RIGHT, fill=tk.Y, padx=20, pady=(0, 20))  

        self.left_frame = tk.Frame(self.frame, bg="#101820")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)   

        #endregion Frames
    
        #region Agenda Section

        label = tk.Label(
            self.left_frame, 
            text="Events today", 
            fg="#fffff0", 
            bg="#101820",
            borderwidth=2,
            relief="solid",
            font=("DejaVu Sans", 20, "bold") 
            )
        label.pack(pady=10)
        label.config(highlightthickness=0, bd=0)
        self.load_events()

        #endregion Agenda Section
    def load_events(self):
        now = datetime.now().astimezone()
        events = self.calendar_service.get_events(now, now + timedelta(days=1))
        for event in events:
            button = create_event_button(self.left_frame, event)
            button.pack(pady=5)

    #region show/hide methods
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()
    #endregion show/hide methods