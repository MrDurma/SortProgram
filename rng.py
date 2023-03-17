import csv
import numpy as np
import time
import os
from csvWriter import CsvWriter

class InputValidator:
    def get_integer_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Oops! That was no valid number. Try again...")

    def validate_range(self, value, min_value, max_value):
        if value < min_value or value > max_value:
            raise ValueError(f"Value must be between {min_value} and {max_value}")

class RngGenerator:
    def generate_random_numbers(range_end):
        return np.random.randint(1, range_end+1, size=range_end)

if __name__ == '__main__':
    # Range should be from 0 - 50000000
    print("This program generates comma-separated values file of random numbers, you define range depending how many numbers you want.")
    print("Passing second argument you can define highest values that can be generated, by default this number is unsigned int")
    print("NOTE: Numbers higher than 10 millions will take 10 seconds + to generate depending on system.")
    
    validator = InputValidator()
    csv_filename = 'randomNumber.csv'
    csv_generator = CsvWriter(csv_filename)

    input_value = validator.get_integer_input("Please enter a number: ")
    validator.validate_range(input_value, 1, 50000000)

    start = time.time()
    random_numbers = RngGenerator.generate_random_numbers(input_value)
    csv_generator.save_csv(random_numbers)
    end = time.time()

    print(f"CSV file '{csv_filename}' saved in '{os.path.abspath(os.path.dirname(__file__))}'")
    print("Execution in seconds:", end - start)
