import uuid

class Position:
    def __init__(self, *args):
        self.id = uuid.uuid4()
        args = args[0]
        self.time = args[0]
        self.x = args[1]
        self.y = args[2]

    def __str__(self):
        return f'P: {self.time} - ({self.x}, {self.y})'