class Robot:

    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.placed = False

    def execute(self, *commands):
        for command in commands:

            if "PLACE" in command:
                self.placed = True
                self.x, self.y, self.direction = command.strip("PLACE ").split(" ")
            if "MOVE" in command:
                if self.direction == "NORTH":
                    self.y = int(self.y) + 1
                elif self.direction == "SOUTH":
                    self.y = int(self.y) - 1
                elif self.direction == "EAST":
                    self.x = int(self.x) + 1
                elif self.direction == "WEST":
                    self.x = int(self.x) - 1
            if "LEFT" in command:
                if self.direction == "NORTH":
                    self.direction = "WEST"
                elif self.direction == "WEST":
                    self.direction = "SOUTH"
                elif self.direction == "SOUTH":
                    self.direction = "EAST"
                elif self.direction == "EAST":
                    self.direction = "NORTH"
            if "RIGHT" in command:
                if self.direction == "WEST":
                    self.direction = "NORTH"
                elif self.direction == "NORTH":
                    self.direction = "EAST"
                elif self.direction == "EAST":
                    self.direction = "SOUTH"
        return self.report()

    def report(self):
        if not self.placed:
            return "I'm not placed yet"
        return ' '.join([str(self.x), str(self.y), self.direction])
