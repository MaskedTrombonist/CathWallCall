import datetime
import tkinter as tk
from pathlib import Path 
from services import dummy_calendar_service
from ui.image_loader import make_icon
from ui.screens.today_screen import TodayScreen
from ui.screens.Month_screen import MonthScreen
from ui.weather_widget import weatherWidget
from services.weather_service import WeatherService



class KioskUI:
    #region screen management

    def show_today(self):
        if "today" not in self.screens:
            self.screens["today"] = TodayScreen(self.content_frame, dummy_calendar_service.DummyCalendarService())
        self._switch_to(self.screens["today"])

    def show_month(self):
        if "month" not in self.screens:
            self.screens["month"] = MonthScreen(self.content_frame)
        self._switch_to(self.screens["month"])

    def _switch_to(self, screen):
        if self.current_screen:
            self.current_screen.hide()
        screen.show()
        self.current_screen = screen
    #endregion screen management

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("CathWallCall Kiosk")
        # Fullscreen kiosk mode.
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#101820")
        #Optional emergency exit for development. 
        self.root.bind("<Escape>", self._exit)
        self.bg = "#101820"  # Dark background color
        self.screens = {}
        self.current_screen = None
        
        #region layout frames
        # Body frame (fills whole window)
        self.body = tk.Frame(self.root)
        self.body.pack(fill=tk.BOTH, expand=True)
        self.body.configure(bg=self.bg)
        
        # Right menu frame (fixed width sidebar)
        self.menu_frame = tk.Frame(self.body, width=220)
        self.menu_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.configure(bg=self.bg)

        # center line frame (for visual separation)
        self.center_line = tk.Frame(self.body, width=2, bg="#fffff0")
        self.center_line.pack(side=tk.RIGHT, fill=tk.Y)

        # Left content frame (where screens go)
        self.content_frame = tk.Frame(self.body)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.content_frame.configure(bg=self.bg)
        # events = self.calendar_service.get_events(now, now + timedelta(days=1))
        #endregion layout frames

        #region menu frame widgets and buttons
        self.clock_label = tk.Label(
            self.menu_frame,
            text="",
            font=("DejaVu Sans", 20, "bold"),
            fg="#fffff0",
            bg=self.bg,
        )
        self.clock_label.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        
        # Initialize weather widget
        weather_service = WeatherService()  # Create an instance of your weather service
        self.weather_widget = weatherWidget(self.menu_frame, service=weather_service)
        
        #region day button
        day_icon_path = Path(__file__).parent / "icons" / "sun.svg"
        make_icon(day_icon_path, color="#fffff0", size=(60, 60), output_path="app/ui/icons/day.png")
        self.day_icon = tk.PhotoImage(file="app/ui/icons/day.png")
        self.day_button = tk.Button(
            self.menu_frame,
            text="Day",
            image=self.day_icon,
            font=("DejaVu Sans", 10, "bold"),
            fg="#fffff0",
            bg=self.bg,
            relief=tk.FLAT,
            bd=0,
            height=100,
            highlightthickness=0,
        )
        self.day_button.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X)
        self.day_button.config(command=self.show_today)
        #endregion day button

        #region calendar button
        calendar_icon_path = Path(__file__).parent / "icons" / "calendar-days.svg"
        make_icon(calendar_icon_path, color="#fffff0", size=(60, 60), output_path="app/ui/icons/calendar-days.png")
        self.calendar_icon = tk.PhotoImage(file="app/ui/icons/calendar-days.png")
        self.calendar_button = tk.Button(
            self.menu_frame,
            text="Calendar",
            image=self.calendar_icon,
            font=("DejaVu Sans", 10, "bold"),
            fg="#fffff0",
            bg=self.bg,
            relief=tk.FLAT,
            bd=0,
            height=100,
            highlightthickness=0,
        )
        self.calendar_button.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X)
        self.calendar_button.config(command=self.show_month)
        #endregion calendar button

        #region settings button
        settings_icon_path = Path(__file__).parent / "icons" / "settings.svg"
        make_icon(settings_icon_path, color="#fffff0", size=(60, 60), output_path="app/ui/icons/settings.png")
        self.settings_icon = tk.PhotoImage(file="app/ui/icons/settings.png")
        self.settings_button = tk.Button(
            self.menu_frame,
            text="Settings",
            image=self.settings_icon,
            font=("DejaVu Sans", 10, "bold"),
            fg="#fffff0",
            bg=self.bg,
            relief=tk.FLAT,
            bd=0,
            height=100,
            highlightthickness=0,
        )
        self.settings_button.pack(side=tk.BOTTOM, padx=10, pady=5, fill=tk.X)
        #endregion settings button

        #endregion menu frame widgets

        self._tick()

    def _tick(self) -> None:
        now = datetime.datetime.now().strftime("%B %-d \n %-I:%M:%S %p")
        self.clock_label.config(text=now)
        self.root.after(1000, self._tick)

    def _exit(self, _event=None) -> None:
        self.root.destroy()
