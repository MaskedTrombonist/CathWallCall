
from datetime import datetime, timedelta
from models.calendar_event import calendar_event

class DummyCalendarService:
    def get_events(self, start_time: datetime, end_time: datetime):
        return [
            calendar_event(
                title="Event 1",
                start_time=start_time + timedelta(hours=1),
                end_time=start_time + timedelta(hours=2),
                location="Location 1",
                description="Description 1"
            ),
            calendar_event(
                title="Event 2",
                start_time=start_time + timedelta(hours=3),
                end_time=start_time + timedelta(hours=4),
                location="Location 2",
                description="Description 2"
            )
        ]