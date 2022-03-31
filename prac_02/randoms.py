import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

''' line 1:
        smallest number = 5, the largest number = 20
    line 2:
        smallest number = 5, the largest number = 9, It can't produce 4
    line 3:
        smallest number = 2.5, the largest number = 5.5 
'''

print(random.randint(1, 100))
