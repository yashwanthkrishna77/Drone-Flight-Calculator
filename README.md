#  Drone Flight Calculator

A modular, command-line Python application for performing common drone
flight calculations. The project is designed to demonstrate the
practical application of basic mathematical and programming concepts
through separate calculation modules and an interactive main menu.

##  Project Overview

The **Drone Flight Calculator** helps users estimate important
flight-related parameters using simple inputs such as battery capacity,
voltage, power consumption, speed, distance, and flight time.

The application provides four main functional modules:

1.  **Flight Time Calculator**
2.  **Range Calculator**
3.  **Battery Calculator**
4.  **Speed Calculator**

The project follows a modular structure, with each calculation
implemented in a separate Python file and integrated through `main.py`.

##  Objectives

-   Apply Python programming concepts to a practical drone-related
    problem.
-   Provide a simple interactive interface for performing flight
    calculations.
-   Divide functionality into reusable and maintainable modules.
-   Validate user inputs before performing calculations.
-   Demonstrate how basic mathematical formulas can support drone flight
    planning.

##  Features

### 1. Flight Time Calculator

Calculates estimated flight time from:

-   Battery capacity in mAh
-   Battery voltage in volts (V)
-   Power consumption in watts (W)

The calculator first converts battery capacity to Ah, calculates battery
energy in Wh, and estimates flight time in minutes.

### 2. Range Calculator

Estimates the drone's flight range using:

-   Drone speed in km/h
-   Flight time in minutes

The flight time is converted to hours before calculating the estimated
distance in kilometers.

### 3. Battery Calculator

Calculates:

-   Total battery energy in Wh
-   Energy consumed during flight
-   Percentage of battery used
-   Remaining battery percentage

The calculation uses battery capacity, voltage, flight time, and power
consumption.

### 4. Speed Calculator

Provides three calculation options:

-   **Calculate Speed** from distance and time
-   **Calculate Distance** from speed and time
-   **Calculate Time** from distance and speed

All results are displayed with appropriate units and rounded values.

### 5. Input Validation

The calculators check that numerical inputs are greater than zero.
Invalid menu choices are also handled by the main application.

##  Project Structure

``` text
Drone-Flight-Calculator/
│
├── main.py
├── flight_time.py
├── range_calculator.py
├── battery_calculator.py
├── speed_calculator.py
└── README.md
```

### Module Responsibilities

  -----------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- -----------------------------------
  `main.py`                           Provides the main menu and connects
                                      all calculator modules

  `flight_time.py`                    Estimates drone flight time

  `range_calculator.py`               Estimates drone flight range

  `battery_calculator.py`             Calculates battery energy and
                                      battery usage

  `speed_calculator.py`               Calculates speed, distance, or time

  `README.md`                         Project documentation
  -----------------------------------------------------------------------

##  Technologies Used

-   **Python 3**
-   Python functions and modules
-   Command-line interface (CLI)
-   Basic mathematical calculations
-   Git/GitHub for version control

No external Python libraries are required by the current implementation.

##  Installation

### Prerequisites

Install **Python 3.x** on your system.

Verify the installation:

``` bash
python --version
```

### Clone the Repository

``` bash
git clone <your-repository-url>
cd Drone-Flight-Calculator
```

## ▶️ How to Run

Run the main program:

``` bash
python main.py
```

The application displays the following menu:

``` text
========================================
       DRONE FLIGHT CALCULATOR
========================================
1. Flight Time Calculator
2. Range Calculator
3. Battery Calculator
4. Speed Calculator
5. Exit
========================================
```

Enter the corresponding menu number to select a calculator.

##  Example Calculations

### Flight Time

If a drone has:

-   Battery capacity: `5000 mAh`
-   Voltage: `22.2 V`
-   Power consumption: `200 W`

The program calculates battery energy and uses it to estimate flight
time.

### Range

If the drone travels at `40 km/h` for `15 minutes`:

``` text
Range = Speed × Time
      = 40 × 0.25
      = 10 km
```

### Speed

If a drone travels `20 km` in `0.5 hours`:

``` text
Speed = Distance / Time
      = 20 / 0.5
      = 40 km/h
```

##  Application Workflow

``` text
Start
  │
  ▼
Display Main Menu
  │
  ├── Flight Time Calculator
  │
  ├── Range Calculator
  │
  ├── Battery Calculator
  │
  ├── Speed Calculator
  │
  └── Exit
        │
        ▼
   Display Result
        │
        ▼
   Return to Main Menu
```

##  Functional Requirements

The current application provides the following functional requirements:

-   Provide an interactive command-line menu.
-   Accept numerical inputs from the user.
-   Validate input values.
-   Calculate estimated flight time.
-   Calculate estimated flight range.
-   Calculate battery energy and battery usage.
-   Calculate speed, distance, and time.
-   Display calculation results with units.
-   Allow the user to perform multiple calculations until selecting
    Exit.

##  Non-Functional Requirements

The project addresses the following non-functional considerations:

### Usability

The application uses a simple numbered menu and clear input prompts.

### Maintainability

Each major calculation is separated into its own Python module, making
the code easier to understand and modify.

### Reliability

Input validation prevents calculations using zero or negative values.

### Resource Efficiency

The application performs lightweight mathematical calculations and does
not require external services or databases.

##  Testing

The current implementation includes input validation within the
calculator modules. For example, non-positive values are rejected before
calculations are performed.

For a complete academic submission, additional unit or validation tests
can be added for each calculator module.

Suggested test cases include:

-   Positive and valid numerical inputs
-   Zero values
-   Negative values
-   Invalid menu choices
-   Boundary and large numerical values
-   Verification of calculation results

##  Academic Project Alignment

This project is structured as a practical programming project with
multiple functional modules, a clear input/output workflow, modular
implementation, validation, and GitHub-based version control.

For the VITyarthi project submission, the project documentation can
additionally include:

-   Problem Statement
-   Objectives
-   Functional Requirements
-   Non-Functional Requirements
-   System Architecture Diagram
-   Workflow Diagram
-   UML diagrams where applicable
-   Testing approach
-   Screenshots/results
-   Challenges and learnings
-   Future enhancements
-   References

##  Future Enhancements

Possible improvements include:

-   Add a graphical user interface (GUI).
-   Add unit tests for all calculation modules.
-   Add configurable battery efficiency and reserve percentage.
-   Include realistic drone power-consumption factors.
-   Add support for different units.
-   Store calculation history.
-   Export calculation results.
-   Add charts for battery usage and flight performance.
-   Add more advanced flight-planning calculations.

##  Calculation Assumptions

The current calculators use simplified mathematical models. Actual drone
performance can vary because of factors such as battery efficiency,
payload, wind, motor efficiency, flight conditions, and other hardware
characteristics.

Therefore, the calculated values should be treated as **estimates rather
than guaranteed real-world flight performance**.



This project was developed as part of the **VITyarthi Build Your Own
Project** activity.

Add your preferred open-source license here, such as MIT License, if you
intend to distribute the project under an open-source license.
