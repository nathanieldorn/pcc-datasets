import csv
from pathlib import Path

import matplotlib.pyplot as plt


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
    return highs


def plot_high_temperatures():
    """Plot the high temperatures"""
    highs = high_temperatures()
    plt.style.use("seaborn-v0_8-darkgrid")
    fig, ax = plt.subplots()
    ax.plot(highs, color="red")

    # plot formatting
    ax.set_title("Daily High Temperatures, July 2021", fontsize=16)
    ax.set_xlabel("", fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=14)

    # show and save plot
    plt.savefig("daily_high_temps_07-2021.png", dpi="figure", bbox_inches="tight")
    plt.show()
