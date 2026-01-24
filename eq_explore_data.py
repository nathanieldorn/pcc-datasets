import json
from datetime import datetime
from pathlib import Path

import plotly.express as px


def read_json():
    """Read earthquake feature data from json files and json metadata"""
    # add/remove comment below for 1 day's data
    # path = Path("eq_data/eq_data_1_day_m1.geojson")
    # add/remove comment below for 30 day data
    path = Path("eq_data/eq_data_30_day_m1.geojson")
    contents = path.read_text(encoding="utf-8")
    eq_data = json.loads(contents)

    # examine earthquakes in the dataset
    eq_dicts = eq_data["features"]
    return eq_dicts


def get_metadata():
    """Reads the json metadata, used by earthquake_world_map() to get json title and timestamp"""
    path = Path("eq_data/eq_data_30_day_m1.geojson")
    contents = path.read_text(encoding="utf-8")
    eq_data = json.loads(contents)
    json_metadata = eq_data["metadata"]
    return json_metadata


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


def get_titles():
    """Creates a list of the earthquake title data for each occurrence to be displayed in hover text"""
    eq_dicts = read_json()
    eq_titles = [earthquake["properties"]["title"] for earthquake in eq_dicts]
    return eq_titles


def earthquake_world_map():
    """Creates a world map of the earthquakes from the file read in read_json()"""
    longitudes, latitudes = get_location_data()
    magnitudes = get_magnitudes()
    eq_titles = get_titles()
    json_metadata = get_metadata()

    # timestamp 13 digits with ms, reduce to 10
    json_timestamp = json_metadata["generated"] / 1000
    json_datetime = f"{datetime.fromtimestamp(json_timestamp)}"

    map_title = json_metadata["title"] + " - " + json_datetime
    fig = px.scatter_geo(
        lat=latitudes,
        lon=longitudes,
        size=magnitudes,
        title=map_title,
        color=magnitudes,
        color_continuous_scale="Viridis",
        labels={"color": "Magnitude", "lat": "Latitude", "lon": "Longitude"},
        projection="natural earth",
        hover_name=eq_titles,
    )

    fig.show()
