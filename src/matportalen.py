from flask import Flask, render_template

import json
from typing import List, Iterator

app = Flask(__name__)


def getAllRestaurantVisits(orgnr):
    list = getEntryList()
    result = {}
    k = 0
    for i in list:
        if i["orgnummer"] and i["orgnummer"] == orgnr:
            result["visit" + str(k)] = i
            k += 1
    return result


def getEntryList() -> List[dict]:
    with open('../data/data.json', 'r') as file:
        jsonBuffer = file.read()
        fullDB = json.loads(jsonBuffer)
    return fullDB["entries"]


def getEntriesForRestaurant(name: str) -> List[dict]:
    entryList = getEntryList()
    result = {}
    return list(filter(lambda e: e["navn"] == name, entryList))


def viewVisits(orgnr):
    allVisits = getAllRestaurantVisits(orgnr)
    visits = {}
    k = 0
    for visit in allVisits:
        thisGrade = getSmileForVisit(allVisits[visit])
        visits["visit" + str(k)] = {"fjes": thisGrade, "dato": allVisits[visit]["dato"]}
        k += 1
    return str(visits)


def getSmileForVisit(visit):
    lol = [visit["karakter1"], visit["karakter2"], visit["karakter3"], visit["karakter4"]]
    haha = 0
    for i in lol:
        if haha < int(i) < 4:
            haha = int(i)
    return str(haha)


@app.route('/')
def home():
    return render_template("restaurant.html", json=str(getEntriesForRestaurant("Abc Thai AS")), title="Matportalen")


@app.route('/<name>')
def restaurant(name):
    return render_template("restaurant.html", title=name, json=str(getEntriesForRestaurant(name)))


if __name__ == '__main__':
    app.run(debug=True)
