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
    return x, y


x, y = reader()
coor = zip(Y, X)
list_coor = list(coor)