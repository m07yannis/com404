print("What is your name?")
name = str(input())

print("How old are you (years)?")
age = int(input())

print("How much do you weight (kg)?")
weight = float(input())

print("How tall are you (m)?")
height = float(input())

print("Calculating bmi...")
bmi = weight / (height * height)
print("Your bmi is", bmi)
