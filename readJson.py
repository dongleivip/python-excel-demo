# -*- coding: UTF-8 -*-
import json


def loadFromJson(path):
    with open(path, "r") as load_f:
        load_dict = json.load(load_f)
        prefix = load_dict["prefix"]
        location = load_dict["location"]
        assets = load_dict["assets"]

        items = []

        for prop in assets:
            template = "{}-{}-{}-{}"
            count = prop["count"]
            for i in range(count):
                code = template.format(
                    prefix, location, prop["category"], str(i + 1).zfill(3)
                )
                items.append({"code": code, "name": prop["name"], "location": location})
        return items


def getDataSource():
    data = loadFromJson("./data.json")
    return data
