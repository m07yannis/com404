#Display life bars
print("Please enter the number of lives remaining:")
lives = int(input())

print("Please enter the energy level:")
energy = int(input())

print("Please enter the shield level:")
shield = int(input())

print("Lives:\t\t", "#" * lives)
print("energy:\t\t", "~" * energy)
print("shield:\t\t", "%" * shield)
