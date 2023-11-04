# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as rfile:
        rdata = json.load(rfile)

    result = [i["score"] * i["weight"] for i in rdata]
    return round(sum(result), 3)

print(task())
