# Practicing with classes

class Position:
    def __init__(self, point = "p0", x_coord = 0, y_coord = 0):
        self.point = point
        self.x_coord = x_coord
        self.y_coord = y_coord

    def increase(self, x_inc, y_inc):
        self.x_coord += x_inc
        self.y_coord += y_inc

    def decrease(self, x_dec, y_dec):
        self.x_coord -= x_dec
        self.y_coord -= y_dec

    def show_pos(self):
        print(f"Coordinates of {self.point} = ({self.x_coord}, {self.y_coord})")