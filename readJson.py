# -*- coding: UTF-8 -*-
import json

Prefix = "CBEX"
DataFilePath = "./data.json"


def getDataForRoom(roomData):
    location = roomData["location"]
    assets = roomData["assets"]

    items = []

    for asset in assets:
        count = asset["count"]
        for i in range(count):
            code = "_".join((Prefix, location, asset["category"], str(i + 1).zfill(3)))
            items.append({"code": code, "name": asset["name"], "location": location})
    return items


def loadFromJson(path):
    allAssets = []
    with open(path, "r") as load_f:
        rooms = json.load(load_f)
        for room in rooms:
            roomAssets = getDataForRoom(room)
            allAssets.append(roomAssets)
    return allAssets


def getDataSource():
    data = loadFromJson(DataFilePath)
    return data
