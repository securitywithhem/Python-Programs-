# # d=√((x_2-x_1)²+(y_2-y_1)²)
# write a program equal distance

import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance between two points is: ",d)
