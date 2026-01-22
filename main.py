from death_valley_highs_lows import plot_temperatures_death_valley
from eq_explore_data import (
    earthquake_world_map,
    get_location_data,
    get_magnitudes,
    read_json,
    readable_json,
)
from sitka_highs import plot_temperatures


def main():
    # plot for sitka_highs
    # plot_temperatures()

    # plot for death_valley_highs_lows
    # plot_temperatures_death_valley()

    # plot for earthquake data
    # readable_json()
    # get_magnitudes()
    earthquake_world_map()


if __name__ == "__main__":
    main()
