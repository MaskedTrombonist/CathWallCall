from datetime import datetime, timedelta
from app.services.calendar_service import CalendarService

svc = CalendarService()
now = datetime.now().astimezone()
events = svc.get_events(now, now + timedelta(days=7))
for e in events:
    print(e.start_time, "-", e.title)