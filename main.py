import unittest
import re
from sys import stdin

class Plateau:
    rovers = []
    m = 0
    n = 0

    def __init__(self, m=0, n=0):
        self.m = m
        self.n = n

    def add_rover(self, rover):
        self.rovers.append(rover)

class Rover:
    x = 0
    y = 0
    heading = ''
    # rover should know plateau dimensions
    m = 0
    n = 0
    command_sequence = []

    def __init__(self, x, y, heading, m, n):
        self.x = int(x)
        self.y = int(y)
        self.m = int(m)
        self.n = int(n)
        self.heading = heading
        self.command_sequence = None

    def move(self):
        if self.heading == 'N':
            self.y = self.y+1 if self.y < self.n else self.y
        elif self.heading == 'E':
            self.x = self.x+1 if self.x <= self.m else self.x
        elif self.heading == 'W':
            self.x = self.x-1 if self.x > 0 else self.x
        elif self.heading == 'S':
            self.y = self.y-1 if self.y > 0 else self.y
        else:
            print("Unknown heading, ignoring move command")

    def turn(self, direction):
        # print(f"{self.heading} -> {direction}")
        if direction == 'L':
            if self.heading == 'N':
                self.heading = 'W'
            elif self.heading == 'E':
                self.heading = 'N'
            elif self.heading == 'W':
                self.heading = 'S'
            elif self.heading == 'S':
                self.heading = 'E'
        elif direction == 'R':
            if self.heading == 'N':
                self.heading = 'E'
            elif self.heading == 'E':
                self.heading = 'S'
            elif self.heading == 'W':
                self.heading = 'N'
            elif self.heading == 'S':
                self.heading = 'W'
        else:
            print("Unknown direction, ignored..")

    def exec_command_sequence(self):
        # print(f"{rover} -- initial position")
        for command in self.command_sequence:
            # print(f"command: {command}")
            if command == 'L' or command == 'R':
                self.turn(command)
            elif command == 'M':
                self.move()
            else:
                print("Unknown command, ignoring..")
            #print(f"{rover}")

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.heading}"

if __name__ == '__main__':
    print("Input plateau dimensions:")
    # parse upper right position of the plateau
    # read plateau dimensions
    l = input().strip()
    if not re.findall("^\d \d$", l):
        exit("Plateau size invalid. should be: m n")

    plateau_size = l.split(" ")
    m = plateau_size[0]
    n = plateau_size[1]
    plateau = Plateau(m, n)

    print(f"Plateau initiated: {m}x{n}")
    print("+--+-----+-----------------------------+++--")

    rover = None
    i = 0
    while True:
        data = input()

        if not data:
            break
        else:
            if i == 0:
                # read rover position
                l = data.strip()
                if not re.findall("^\d \d (N|E|W|S)$", l):
                    print("Rover position invalid. should be: digit digit letter (example '1 2 N')")
                else:
                    rover_position = l.split(" ")
                    if int(rover_position[0]) < 0 or rover_position[0] > m:
                        print("Rover x is out of bounds")
                    elif int(rover_position[1]) < 0 or rover_position[1] > n:
                        print("Rover y is out of bounds")
                    else:
                        rover = Rover(rover_position[0],
                            rover_position[1],
                            rover_position[2],
                            m,
                            n
                        )
                        i +=1

            elif i == 1:
                # read rover command sequence
                l = data.strip()
                if not re.findall("^(L|R|M| )*$", l):
                    print("Rover command sequence invalid. should be a sequence of space-separated letters (L, R or M)")
                else:
                    rover.command_sequence = l.split(" ")
                    plateau.add_rover(rover)
                    i = 0
                    rover = None
                    print("New rover saved.\n Input another rover info:")

    print("+--+-----+-----------------------------+++--")
    print(f"rovers on the plateau: {len(plateau.rovers)}")
    for rover in plateau.rovers:
        rover.exec_command_sequence()
        print(rover)

    print("+--+-----+-----------------------------+++--")
    print("Mars explored, no alien life found.")
