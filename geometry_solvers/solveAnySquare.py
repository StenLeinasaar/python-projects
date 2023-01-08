from math import sqrt


class Square:

    # If there is no value, set to None
    def __init__(self, a, perimeter, area):
        self.side = a
        self.perimeter = perimeter
        self.area = area
        self.solve_square()

    def solve_square(self):
        # begin checking if you have a side
        if self.side:
            # If there is a side then just calculate the perimeter and area
            if not self.area:
                self.set_area()
            if not self.perimeter:
                self.set_perimeter()
        else:
            # THere is no side. Get side. 
            self.set_side()
            # then call the method again to set perimeter and area when needed
            self.solve_square()

        return True

    def set_side(self):
        # check if there is an area. 
        if self.area:
            self.side = sqrt(self.area)
        elif self.perimeter:
            self.side = self.perimeter/4

        return True
    def get_side(self):
        return self.side

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    def set_perimeter(self):
        self.perimeter = self.side * 4
        return True

    def set_area(self):
        self.area = self.side ** 2
        return True

if __name__ == "__main__":
    pass