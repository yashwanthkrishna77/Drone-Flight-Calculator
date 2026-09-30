from flight_time import calculate_flight_time
from range_calculator import calculate_range
from battery_calculator import battery_calculator
from speed_calculator import speed_calculator


while True:
    print("\n========================================")
    print("       DRONE FLIGHT CALCULATOR")
    print("========================================")
    print("1. Flight Time Calculator")
    print("2. Range Calculator")
    print("3. Battery Calculator")
    print("4. Speed Calculator")
    print("5. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculate_flight_time()

    elif choice == "2":
        calculate_range()

    elif choice == "3":
        battery_calculator()

    elif choice == "4":
        speed_calculator()

    elif choice == "5":
        print("\nThank you for using Drone Flight Calculator!")
        break

    else:
        print("\nInvalid choice. Please try again.")
