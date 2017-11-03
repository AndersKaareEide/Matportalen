from flask import Flask, render_template

import json

app = Flask(__name__)

def getAllRestaurantVisits(orgnr):
    with open('../data/data.json', 'r') as f:
        lol = f.read()
        fullDB = json.loads(lol)
    list = fullDB["entries"]
    result = {}
    k = 0
    for i in list:
        if i["orgnummer"]:
            if i["orgnummer"] == orgnr:
                result["visit" + str(k)] = i
                k += 1
    return result

def viewVisits(orgnr):
    allVisits = getAllRestaurantVisits(orgnr)
    visits = {}
    k = 0
    for visit in allVisits:
        thisGrade = getSmileForVisit(allVisits[visit])
        visits["visit"+str(k)] = {"fjes": thisGrade, "dato": allVisits[visit]["dato"]}
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
    return render_template("restaurant.html", json=viewVisits("985129576"), title="Matportalen")


@app.route('/<name>')
def restaurant(name):
    return render_template("restaurant.html", title=name)


if __name__ == '__main__':
    app.run(debug=True)



