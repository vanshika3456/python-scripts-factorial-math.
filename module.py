#task2
# Using the Math Module for Calculations

import math
n= int(input("enter the number:"))
if n<0:
    print("Logarithm and square root are only defined for positive numbers.")
else:
     square_root=math.sqrt(n)
     nature_log=math.log(n)
     sine_value=math.sin(n)
     print("square root",square_root)
     print("nature_log",nature_log)
     print("sine",sine_value)