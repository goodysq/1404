from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    menu()
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            choose_taxi(current_taxi, taxis)
        elif menu_choice == "d":
            drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        menu()
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def menu():
    """Display menu"""
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(current_taxi, taxis):
    """Choose from a list of available taxis,"""
    print("Taxis available: ")
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(current_taxi, total_bill):
    """Choose how far to drive"""
    if current_taxi:
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")


if __name__ == '__main__':
    main()
