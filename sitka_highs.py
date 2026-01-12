import csv
from pathlib import Path


def read_csv():
    """Reads the csv and creates a list of the row data and headers"""
    path = Path("weather_data/sitka_weather_07-2021_simple.csv")
    lines = path.read_text(encoding="utf-8").splitlines()

    reader = csv.reader(lines)
    headers = next(reader)

    """for i, header in enumerate(headers):
       print(i, header)"""

    return reader


def high_temperatures():
    """Extracts the high temperatures from the list returned by read_csv"""
    reader = read_csv()
    highs = [int(row[4]) for row in reader if row[4] != ""]
    print(highs)
