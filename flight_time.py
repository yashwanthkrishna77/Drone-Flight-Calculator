def calculate_flight_time():
    print("\n---------- FLIGHT TIME CALCULATOR ----------")

    capacity = float(input("Enter battery capacity (mAh): "))
    voltage = float(input("Enter battery voltage (V): "))
    power = float(input("Enter power consumption (W): "))

    if capacity <= 0 or voltage <= 0 or power <= 0:
        print("Values must be greater than zero.")
        return

    capacity_ah = capacity / 1000

    battery_energy = voltage * capacity_ah

    flight_time_hours = battery_energy / power
    flight_time_minutes = flight_time_hours * 60

    print("\nBattery Energy:", round(battery_energy, 2), "Wh")
    print("Estimated Flight Time:",
          round(flight_time_minutes, 2), "minutes")
