# Program to illustrate pi, sqrt, sin and cos functions
import math
# Using pi
print("Value of pi:", math.pi)
# Using sqrt
num = 64
print("Square root of", num, "is:", math.sqrt(num))
# Using sin and cos
angle = 90                    # angle in degrees
angle_rad = math.radians(angle)
print("Sin of", angle, "degrees:", math.sin(angle_rad))
print("Cos of", angle, "degrees:", math.cos(angle_rad))
# Extra example: Area of circle
radius = 10
area = math.pi * radius * radius
print("Area of a circle with radius", radius,"is:",area)