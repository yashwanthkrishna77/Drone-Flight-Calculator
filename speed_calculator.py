def speed_calculator():
    print("\n---------- SPEED CALCULATOR ----------")
    print("1. Calculate Speed")
    print("2. Calculate Distance")
    print("3. Calculate Time")

    choice = input("Enter your choice: ")

    if choice == "1":
        distance = float(input("Enter distance (km): "))
        time = float(input("Enter time (hours): "))

        if distance <= 0 or time <= 0:
            print("Values must be greater than zero.")
            return

        speed = distance / time

        print("\nSpeed:",
              round(speed, 2), "km/h")

    elif choice == "2":
        speed = float(input("Enter speed (km/h): "))
        time = float(input("Enter time (hours): "))

        if speed <= 0 or time <= 0:
            print("Values must be greater than zero.")
            return

        distance = speed * time

        print("\nDistance:",
              round(distance, 2), "km")

    elif choice == "3":
        distance = float(input("Enter distance (km): "))
        speed = float(input("Enter speed (km/h): "))

        if distance <= 0 or speed <= 0:
            print("Values must be greater than zero.")
            return

        time = distance / speed

        print("\nTime:",
              round(time, 2), "hours")

    else:
        print("Invalid choice.")
