def calculate_range():
    print("\n---------- RANGE CALCULATOR ----------")

    speed = float(input("Enter drone speed (km/h): "))
    flight_time = float(input("Enter flight time (minutes): "))

    if speed <= 0 or flight_time <= 0:
        print("Values must be greater than zero.")
        return

    flight_time_hours = flight_time / 60

    distance = speed * flight_time_hours

    print("\nEstimated Flight Range:",
          round(distance, 2), "km")
