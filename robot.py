def execute(*commands):
    x = None
    y = None
    direction = None
    placed = False

    for command in commands:

        if "PLACE" in command:
            placed = True
            x, y, direction = command.strip("PLACE ").split(" ")
        if "MOVE" in command:
            if direction == "NORTH":
                y = int(y) + 1
            elif direction == "SOUTH":
                y = int(y) - 1
            elif direction == "EAST":
                x = int(x) + 1
            elif direction == "WEST":
                x = int(x) - 1
        if "LEFT" in command:
            if direction == "NORTH":
                direction = "WEST"
            elif direction == "WEST":
                direction = "SOUTH"
            elif direction == "SOUTH":
                direction = "EAST"
            elif direction == "EAST":
                direction = "NORTH"
        if "RIGHT" in command:
            if direction == "WEST":
                direction = "NORTH"
            elif direction == "NORTH":
                direction = "EAST"
            elif direction == "EAST":
                direction = "SOUTH"
    return build_return(x, y, direction, placed)


def build_return(x, y, direction, placed):
    if not placed:
        return "I'm not placed yet"
    return ' '.join([str(x), str(y), direction])
