class Task:
    def __init__(self, title: str, description: str = "", due_date: str = "") -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 0 #0 for not started, 1 for in progress, 2 for completed, 3 for blocked
        self.start_date = ""
        self.completion_date = ""
        self.block_reason = ""

    def status_to_string(self) -> str:
        status_map = {
            0: "Not Started",
            1: "In Progress",
            2: "Completed",
            3: "Blocked"
        }
        return status_map.get(self.status, "Unknown")

    def start(self, date: str) -> None:
        self.start_date = date
        self.status = 1 # In Progress

    def complete(self, date: str) -> None:
        self.completion_date = date
        self.status = 2 # Completed

    def block(self, reason: str) -> None:
        self.status = 3 # Blocked
        self.block_reason = reason