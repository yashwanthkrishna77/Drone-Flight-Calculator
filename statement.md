# Project Statement: Drone Flight Calculator

## Problem Statement

Anyone who flies a drone, whether a hobbyist, a student building their first quadcopter, or someone planning a small aerial survey, keeps running into the same handful of questions before takeoff:

- How long will this battery actually keep the drone in the air?
- How far can I go at a given speed before I need to turn back?
- How much of the battery will this flight use up?
- If I know the distance and the speed, how long will the trip take?

The formulas behind these answers are simple, but they involve unit conversions that are easy to get wrong when done by hand (mAh to Ah, minutes to hours, Ah and volts to watt-hours). Doing them on paper or in a phone calculator mid-planning is slow and error-prone. A wrong number here isn't just an inconvenience. It can mean a drone that runs out of charge far from home.

This project puts those calculations in one small, easy-to-use program. You type in the numbers you already know, and it handles the maths and the unit conversions for you.

## Scope of the Project

**What the project covers**

- A command-line application written in Python, run from a simple numbered menu.
- Four calculators, each in its own module:
  1. **Flight time**, estimated from battery capacity (mAh), voltage (V) and power consumption (W).
  2. **Range**, estimated from speed (km/h) and flight time (minutes).
  3. **Battery usage**, showing the battery's total energy, the energy a flight uses, and the percentage used and remaining.
  4. **Speed, distance and time**, solving for whichever one of the three is missing.
- Input validation, so zero or negative values are rejected with a clear message.
- A menu that keeps running, so you can do several calculations in one session and exit when you're done.

**What the project does not cover**

- It gives theoretical estimates only. It assumes steady power draw and steady speed, and it doesn't account for wind, payload, temperature, battery ageing or aggressive manoeuvres.
- It doesn't connect to a real drone, read telemetry, or plan routes.
- It has no graphical interface, database or user accounts. It is a focused calculation tool.

## Target Users

- **Drone hobbyists** who want a quick sanity check before a flight.
- **Students and beginners** learning how battery energy, power and flight time relate to each other.
- **DIY drone builders** comparing different battery and motor combinations on paper before buying parts.
- **Educators** who need a small, readable example of modular Python for teaching.

## High-Level Features

- **Four focused modules:** flight time, range, battery and speed, each easy to read and change on its own.
- **Automatic unit handling:** you enter values in the units you already have (mAh, minutes, km/h), and the program does the conversions.
- **Clear input and output:** every calculator asks for exactly what it needs and prints labelled, rounded results.
- **Basic input validation:** invalid values are caught before they can produce nonsense results.
- **Simple, repeatable workflow:** pick an option, enter values, read the result, and go back to the menu.
- **No setup needed:** plain Python with no external libraries.

## Why This Project Matters

The idea is small, but it solves a real, everyday planning problem. It also shows the course concepts in practice: splitting a program into modules, handling user input, validating data, and turning real-world formulas into working code.
