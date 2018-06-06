# -*- coding: utf-8 -*-
import sys


WEST = "WEST"
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
PLACE = "PLACE"
MOVE = "MOVE"
LEFT = "LEFT"
RIGHT = "RIGHT"

x_lower_limit = 0
y_lower_limit = 0
x_upper_limit = 4
y_upper_limit = 4


class Robot:

    turn_states = {
        RIGHT: {
            WEST: NORTH,
            NORTH: EAST,
            EAST:  SOUTH,
            SOUTH: WEST
        },
        LEFT: {
            NORTH: WEST,
            WEST: SOUTH,
            SOUTH: EAST,
            EAST: NORTH
        }
    }

    def __init__(self, mapa):
        self.x = None
        self.y = None
        self.direction = None
        self.placed = False
        self.commands_dict = {
            MOVE: self.move,
            LEFT: self.turn,
            RIGHT: self.turn
        }

    def execute(self, *commands):
        for command in commands:
            if PLACE in command:
                self.place(command)
            if command in self.commands_dict.keys():
                self.commands_dict[command](command)
        return self.report()

    def place(self, command):
        self.placed = True
        self.x, self.y, self.direction = command.strip("PLACE ").split(" ")

    def turn(self, command):
        self.direction = self.turn_states[command][self.direction]

    def check_limit(self, x, y):
        if x < x_lower_limit:
            x = x_lower_limit
        if y < y_lower_limit:
            y = y_lower_limit
        if x > x_upper_limit:
            x = x_upper_limit
        if y > y_upper_limit:
            y = y_upper_limit
        return x, y

    def move(self, command):
        move = {
            NORTH: (0,  1),
            WEST: (-1,  0),
            SOUTH: (0, -1),
            EAST: (1, 0)
        }
        self.x, self.y = self.check_limit(int(self.x) + move[self.direction][0], int(self.y) + move[self.direction][1])

    def report(self):
        self.print_map()
        if not self.placed:
            return "I'm not placed yet"
        return ' '.join([str(self.x), str(self.y), self.direction])

    def print_map(self):
        x = int(self.x) if self.x else self.x
        y = 4 - int(self.y) if self.y else self.y
        for i in reversed(range(0, 5)):
            sys.stdout.write('{} '.format(i))
            for j in reversed(range(0, 5)):
                if i == x and j == y:
                    sys.stdout.write('R ')
                else:
                    sys.stdout.write('# ')
            print('')
        print('  0 1 2 3 4')
        print('- - - - - -')
