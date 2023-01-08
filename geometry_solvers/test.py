
from solveAnySquare import Square
import time

print("making a square object")
obj =  Square(None, 18, None)

print("The area of the square is: " , obj.get_area())
time.sleep(2)
print("The perimeter of the square is: ", obj.get_perimeter())
time.sleep(2)
print("The side of a square is:" , obj.get_side())
time.sleep(2)


del obj

try:
    print("Here is the object", obj)
except Exception as e:
    print("Object does not exist")