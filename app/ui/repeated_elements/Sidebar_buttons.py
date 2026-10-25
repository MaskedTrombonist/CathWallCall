import tkinter as tk
from ui.colors import background_color, foreground_color
from ui.image_loader import make_icon

def create_sidebar_button(menu_frame, button_name, icon_name, icon_path, command, side):
    make_icon(icon_path, color=foreground_color, size=(60, 60), output_path=f"app/ui/icons/{icon_name}.png")
    icon = tk.PhotoImage(file=f"app/ui/icons/{icon_name}.png")
    button = tk.Button(
        menu_frame,
        text=button_name,
        image=icon,
        font=("DejaVu Sans", 10, "bold"),
        fg=foreground_color,
        bg=background_color,
        relief=tk.FLAT,
        bd=0,
        height=100,
        highlightthickness=0,
        command=command
    )
    button.pack(side=side, padx=10, pady=5, fill=tk.X)
    button.image = icon
    return button

