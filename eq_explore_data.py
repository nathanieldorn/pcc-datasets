import json
from pathlib import Path

import plotly.express as px


def read_json():
    """Read data from json files within eq_data directory"""
    path = Path("eq_data/eq_data_1_day_m1.geojson")
    contents = path.read_text(encoding="utf-8")
    eq_data = json.loads(contents)
    # return eq_data

    # examine earthquakes in the dataset
    eq_dicts = eq_data["features"]
    return eq_dicts


def readable_json():
    """Improves the human readability of the json source data"""
    path = Path("eq_data/readable_eq_data.geojson")
    readable_contents = json.dumps(read_json(), indent=4)
    path.write_text(readable_contents)


def get_magnitudes():
    """Creates a list of earthquake magnitudes"""
    eq_dicts = read_json()
    magnitudes = [earthquake["properties"]["mag"] for earthquake in eq_dicts]
    return magnitudes


def get_location_data():
    """Creates a list of longitudinal and latitudinal coordinates, returning a list for each"""
    eq_dicts = read_json()
    longitudes = [earthquake["geometry"]["coordinates"][0] for earthquake in eq_dicts]
    latitudes = [earthquake["geometry"]["coordinates"][1] for earthquake in eq_dicts]
    return longitudes, latitudes


def earthquake_world_map():
    longitudes, latitudes = get_location_data()
    title = "Global Earthquakes"
    fig = px.scatter_geo(lat=latitudes, lon=longitudes, title=title)
    fig.show()
