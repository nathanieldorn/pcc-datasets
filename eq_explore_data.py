import json
from pathlib import Path


def read_json():
    """Read data from json files within eq_data directory"""
    path = Path("eq_data/eq_data_1_day_m1.geojson")
    contents = path.read_text(encoding="utf-8")
    eq_data = json.loads(contents)
    return eq_data


def readable_json():
    """Improves the human readability of the json source data"""
    path = Path("eq_data/readable_eq_data.geojson")
    readable_contents = json.dumps(read_json(), indent=4)
    path.write_text(readable_contents)
