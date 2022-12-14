#! usr/bin/env python

from sys import argv
from os.path import exists
import json 

script, in_file, out_file = argv

data = json.load(open(in_file))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["Longitude"], d["Latitude"]],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w')
json.dump(geojson, output)

# python json2geojson.py crime_records.json crime_records.geojson