from openpyxl import load_workbook
import geojson as jsn
import random as rd
from pymongo import MongoClient
from bson.json_util import dumps, loads
import mongo_to_geojson
import pprint

def reader():
    wb = load_workbook('./data.xlsx')
    sheet = wb['Лист1']
    x = []
    y = []
    for i in range(1, 129):
            a = sheet.cell(row=i+1, column=2).value
            X.append(float(a))
    for i in range(1, 129):
            a = sheet.cell(row=i+1, column=3).value
            Y.append(float(a))
    coor = zip(Y, X)
    list_coor = list(coor)
    return list_coor

def list2geojson(list):
    features = []
    for i in list:
        tupe_road = ["urb", "rur", "hway"]
        width_road = [5, 7, 10, 12, 18]
        long_road = rd.randint(100, 150)
        surface = ["asp", "crt", "gra", "grnd"]
        features.append(jsn.Feature(geometry=jsn.Point(i), properties={"type": rd.choice(tupe_road),
                                                                       "width": rd.choice(width_road),
                                                                       "long": long_road,
                                                                       "face": rd.choice(surface),
                                                                       }))
    feature_collection = jsn.FeatureCollection(features=features)
    with open('All_points.geojson', 'w') as f:
        jsn.dump(feature_collection, f)
    with open('JSON_for_DB.json', 'w') as f:
        jsn.dump(features, f)

list = reader()
list2geojson(list)
