import csv
import os

class CsvWriter:
    def __init__(self, filename):
        self.filename = filename

    def save_csv(self, data):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.filename)
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([data])
        