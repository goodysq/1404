from unreliable_car import UnreliableCar


def main():
    """test UnreliableCar class"""
    car_reliable = UnreliableCar("good", 100, 80)
    car_unreliable = UnreliableCar("bad", 100, 20)

    for i in range(1, 10):
        print("-----", i, "attempt-----")
        print(car_reliable.name, car_reliable.drive(i))
        print(car_unreliable.name, car_unreliable.drive(i))

    print(car_reliable)
    print(car_unreliable)


if __name__ == '__main__':
    main()
