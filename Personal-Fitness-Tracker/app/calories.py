# calories.py - Handles meal logging and calorie tracking

import csv
import datetime

DATA_FILE = "../data/calories.csv"

def log_meal():
    meal_name = input("Enter meal name: ")
    calories = input("Enter calorie count: ")
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([meal_name, calories, str(datetime.date.today())])
    print("Meal logged successfully!")
