import tkinter as tk
from ui.colors import background_color, foreground_color

def create_event_button(parent,event):
    button = tk.Button(
        parent,
        text=f"{event.start_time} - {event.title}",
        fg=foreground_color,
        bg=background_color,
        font=("DejaVu Sans", 14, "bold"),
        borderwidth=2,
        relief="solid"
    )
    return button
