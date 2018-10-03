#Read radius from user
import math

print("Please enter radius")
radius = float(input())

# Calculate area and circimference
area = math.pi * (radius * radius)
circumference = 2 * math.pi * radius

#Display the results
print("Area is" , area)
print("Circumference is", circumference)
