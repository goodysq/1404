"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""


def calculate_bonus(sales):
    while sales >= 0:
        if sales < 1000:
            bonus = 0.1
        elif sales >= 1000:
            bonus = 0.15
        print("The bonus is $", int(bonus * sales))
        sales = float(input("Enter sales: $"))


def main():
    sales = float(input("Enter sales: $"))
    while sales < 0:
        print("This is invalid bonys, try again")
        sales = float(input("Enter sales: $"))
    calculate_bonus(sales)


main()
