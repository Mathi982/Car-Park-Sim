# Car-Park-Sim
Car Park Simulator
A Python-based car park management simulation with two user interfaces: a command-line interface (CLI) and a graphical user interface (GUI). The system, written in Python, allows users to simulate car park operations such as entering and exiting a car park, viewing available parking spaces, and querying parking records by ticket number.

Key components of the system include:

CarPark.py: This is the core module that manages the car park logic. It handles data storage using a CSV file (CarParkRecord.csv) to keep track of car parking records. This module includes functions for various car park operations like entering and exiting the car park, calculating parking fees, and managing parking spaces.

cmdui.py: This script provides a command-line interface for interacting with the car park system. It offers a menu-driven experience where users can choose to perform actions like parking a car, exiting the car park, viewing available parking spaces, and querying parking records. The script uses CarPark.py for all underlying functionalities.

gui.py: This script creates a graphical user interface for the car park system using the tkinter library. It offers a more user-friendly and interactive way to perform car park operations similar to those available in the CLI. This GUI version also uses CarPark.py for all its functionalities.

Features of the Car Park Management System:

Dynamic Parking Management: Tracks and manages parking spaces, handling car entries and exits.
Hourly Rate Calculation: Calculates parking fees based on an hourly rate.
Data Persistence: Maintains parking records in a CSV file, allowing data to persist across sessions.
User Interfaces: Offers both CLI and GUI options, catering to different user preferences.
Error Handling and Validations: Includes basic error handling and input validations for a smoother user experience.
