import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

dates, highs, lows = [], [], []


def read_csv():
    """Read the referenced csv file and extract headers and rows"""
    path = Path("weather_data/death_valley_2021_simple.csv")
    lines = path.read_text(encoding="utf-8").splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    return reader


def extract_dates_highs_lows():
    """Extract the high and low temperatures by date and log missing data in file"""
    reader = read_csv()
    missing_data = ""

    for row in reader:
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            missing_data += (
                f"Missing data for {datetime.strptime(row[2], '%Y-%m-%d')}\n"
            )
        else:
            dates.append(datetime.strptime(row[2], "%Y-%m-%d"))
            highs.append(high)
            lows.append(low)

    if len(missing_data) > 0:
        with open("missing_data_death_valley.txt", "w") as file:
            file.write(missing_data)


def plot_temperatures_death_valley():
    """Plot the high and low temperatures by date for the file referenced in read_csv"""
    extract_dates_highs_lows()
    title = "Daily High and Low Temperaturs, 2021\nDeath Valley, CA"
    plt.style.use("seaborn-v0_8-darkgrid")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red", alpha=0.5)
    ax.plot(dates, lows, color="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.2)

    # plot formatting
    ax.set_title(title, fontsize=20, color="green")
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=14)

    # show and save plot
    plt.savefig(
        "daily_high_low_temps_death_valley_2021.png", dpi="figure", bbox_inches="tight"
    )
    plt.show()
