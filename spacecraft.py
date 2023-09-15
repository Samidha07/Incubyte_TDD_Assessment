
class Spacecraft:
    def __init__(self, x=0, y=0, z=0, direction='N'):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'Up':
            pass  # Already facing Up, no change
        elif self.direction == 'Down':
            pass  # Already facing Down, no change

    def turn_down(self):
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'Up':
            pass  # Already facing Up, no change
        elif self.direction == 'Down':
            pass  # Already facing Down, no change

# interactive_control.py
from spacecraft import Spacecraft

def main():
    spacecraft = Spacecraft()
    print("Chandrayaan 3 Lunar Craft Control")
    print(f"Initial Position: ({spacecraft.x}, {spacecraft.y}, {spacecraft.z})")
    print(f"Initial Direction: {spacecraft.direction}")

    while True:
        command = input("Enter a command (f/b/l/r/u/d/q to quit): ").strip().lower()

        if command == 'q':
            break

        if command in ['f', 'b', 'l', 'r', 'u', 'd']:
            if command == 'f':
                spacecraft.move_forward()
            elif command == 'b':
                spacecraft.move_backward()
            elif command == 'l':
                spacecraft.turn_left()
            elif command == 'r':
                spacecraft.turn_right()
            elif command == 'u':
                spacecraft.turn_up()
            elif command == 'd':
                spacecraft.turn_down()

            print(f"New Position: ({spacecraft.x}, {spacecraft.y}, {spacecraft.z})")
            print(f"New Direction: {spacecraft.direction}")
        else:
            print("Invalid command. Please enter f, b, l, r, u, d, or q to quit.")

if __name__ == '__main__':
    main()
