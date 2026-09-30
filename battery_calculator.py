def battery_calculator():
    print("\n---------- BATTERY CALCULATOR ----------")

    capacity = float(input("Enter battery capacity (mAh): "))
    voltage = float(input("Enter battery voltage (V): "))
    flight_time = float(input("Enter flight time (minutes): "))
    power = float(input("Enter power consumption (W): "))

    if capacity <= 0 or voltage <= 0 or flight_time <= 0 or power <= 0:
        print("Values must be greater than zero.")
        return

    capacity_ah = capacity / 1000

    battery_energy = capacity_ah * voltage

    energy_used = power * (flight_time / 60)

    remaining_energy = battery_energy - energy_used

    if remaining_energy < 0:
        remaining_energy = 0

    battery_used_percent = (energy_used / battery_energy) * 100

    if battery_used_percent > 100:
        battery_used_percent = 100

    remaining_percent = 100 - battery_used_percent

    print("\nBattery Energy:",
          round(battery_energy, 2), "Wh")

    print("Energy Used:",
          round(energy_used, 2), "Wh")

    print("Battery Used:",
          round(battery_used_percent, 2), "%")

    print("Remaining Battery:",
          round(remaining_percent, 2), "%")
