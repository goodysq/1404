import random

num_of_each_line = 6
max_num = 45
min_num = 1


def mian():
    """get sets of random numbers"""
    num_quick_picks = int(input("How many quick picks? "))
    while num_quick_picks <= 0:
        print("Invalid")
        num_quick_picks = input("How many quick picks? ")

    for i in range(num_quick_picks):
        quick_picks = []

        for j in range(num_of_each_line):
            number = random.randint(min_num, max_num)

            # Each line (quick pick) should not contain any repeated number.
            while number in quick_picks:
                number = random.randint(min_num, max_num)
            quick_picks.append(number)

        # Each line of numbers should be displayed in sorted (ascending) order.
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


mian()
