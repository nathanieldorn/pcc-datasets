import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


def read_csv():
    """Reads the csv and creates a list of the row data and headers"""
    # Uncomment depending on which file is to be read
    # path = Path("weather_data/sitka_weather_07-2021_simple.csv")
    path = Path("weather_data/sitka_weather_2021_simple.csv")
    lines = path.read_text(encoding="utf-8").splitlines()

    reader = csv.reader(lines)
    # Uncomment if headers are neeeded
    headers = next(reader)

    return reader


def extract_dates():
    """Extracts the date of each high temperature in the list returned by read_csv"""
    reader = read_csv()
    dates = [datetime.strptime(row[2], "%Y-%m-%d") for row in reader]
    return dates


def high_temperatures():
    """Extracts the high temperatures from the list returned by read_csv"""
    reader = read_csv()
    highs = [int(row[4]) for row in reader if row[4] != ""]
    return highs


def low_temperatures():
    """Extracts the low temperatures from the list returned by read_csv"""
    reader = read_csv()
    lows = [int(row[5]) for row in reader if row[5] != ""]
    return lows


def plot_temperatures():
    """Plot the temperatures, high and low, by date"""
    highs = high_temperatures()
    dates = extract_dates()
    lows = low_temperatures()
    plt.style.use("seaborn-v0_8-darkgrid")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red", alpha=0.5)
    ax.plot(dates, lows, color="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.2)

    # plot formatting
    ax.set_title("Daily High and Low Temperatures, 2021", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=14)

    # show and save plot
    plt.savefig("daily_high_low_temps_2021.png", dpi="figure", bbox_inches="tight")
    plt.show()
