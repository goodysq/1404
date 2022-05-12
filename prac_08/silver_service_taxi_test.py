from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class"""
    taxi = SilverServiceTaxi("Taxi", 100, 20)
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()
