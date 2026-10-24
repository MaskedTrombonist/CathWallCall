# TODO: create an event button UI element that can be placed on the today screen. 

import tkinter as tk

def create_event_button(parent,event):
    button = tk.Button(
        parent,
        text=f"{event.start_time} - {event.title}",
        fg="#fffff0",
        bg="#101820",
        font=("DejaVu Sans", 14, "bold"),
        borderwidth=2,
        relief="solid"
    )
    return button
