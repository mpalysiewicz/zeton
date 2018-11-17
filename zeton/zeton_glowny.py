"""
Aplikacja: system żetonowy

"""

from flask import Flask
import json

punkty = 16
with open('dane.json', 'w') as plik:
    json.dump(punkty,plik)

import json
app = Flask(__name__)

@app.route('/')
def hello():
    global punkty
    with open('dane.json', 'r') as plik:
        punkty = json.load(plik)

    return f'Aktualnie masz {punkty} punktów!'


def dodaj_punkt(nowe_punkty):
    return nowe_punkty




if __name__ == '__main__':
    app.run()