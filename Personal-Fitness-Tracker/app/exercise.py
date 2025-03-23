# exercise.py - Handles workout logging and tracking

import csv
import datetime

DATA_FILE = "../data/exercise.csv"

def log_workout():
    workout_type = input("Enter workout type: ")
    duration = input("Enter duration in minutes: ")
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([workout_type, duration, str(datetime.date.today())])
    print("Workout logged successfully!")
