LOWER = 33
UPPER = 127
character = input("Enter a character: ")
print(f"The ASCII code for {character} is {ord(character)}")
number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
print(f"The character for {number} is {chr(number)}")

for num in range(LOWER, UPPER + 1):
    print(f"{num:>3d} {chr(num)}")
