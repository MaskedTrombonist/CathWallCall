import tkinter as tk
from ui import KioskUI


def main() -> None:
    app_root = tk.Tk()
    KioskUI(app_root)
    app_root.mainloop()


if __name__ == "__main__":
    main()


