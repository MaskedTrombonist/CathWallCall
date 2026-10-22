from person import person

class adult(person):
    def __init__(self, name, parent, age, administrator):
        super().__init__(name, age)
        self.parent = parent #in future this will allow the adult to approve chores for children
        self.administrator = administrator #in future this will allow the adult to manage other users