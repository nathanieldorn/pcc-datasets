# A Data Visualization Project with Matplotlib and Plotly
### Using Data Sourced from CSV and Geo JSON Files
Add or remove comments from `main.py` to run functions for either Sitka or Death Valley. Only one may be run at a time. Output will be saved to a `.png` file as well as displayed.

## Sitka High and Low Temperatures
Displays the daily high and low temperatures with fill between each plot. Output is saved to the file, `daily_high_temps_2021.png`. The data is sourced from the Sitka weather CSV files within the `weather_data` directory.

## Death Valley High and Low Temperatures
Displays the daily high an dlow temperatures with fill between each plot. Output is saved to the file, `daily_high_low_temps_death_valley_2021.png`. The data is sourced from the Death Valley CSV file within the `weather_data` directory. If any rows are missing required data, they are skipped and logged in `missing_data_death_valley.txt`.

![Daily High and Low Death Valley 2021](https://github.com/nathanieldorn/pcc-datasets/blob/main/daily_high_low_temps_death_valley_2021.png)

## Earthquake World Map
Displays a world map of earthquakes over a 30 day period. The data is sourced from the `.geojson` files in the `eq_data` directory. The map has been customized to display the file's timestamp and features hover text data for each earthquake, including approximate location description, coordinates, and magnitude. Magnitude is denoted by the size of each occurence as well as its color, following the legend on the right.

![Earthquake World Map - Last 30 Days](https://github.com/nathanieldorn/pcc-datasets/blob/main/earthquake_world_map.png)
