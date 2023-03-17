import os
import csv

class CsvReader:
    """Reads a CSV file, returns all values in a list"""
    def __init__(self):
        filename = 'randomNumber.csv'
        self.filename = filename

    def read_csv_file(self):
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.filename)
            with open(path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for number_list in reader:
                    return number_list