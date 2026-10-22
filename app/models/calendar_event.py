from person import person

class calendar_event():
    def __init__(self, title, start_time, end_time, location, description, people):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.description = description
        self.people = people or [] #list of person objects associated with the event

    def get_colors(self):
        return [person.color.hex_value for person in self.people]
    