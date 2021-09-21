from flask import Flask
import requests
import json
from flask import jsonify
from model import db, Joke, app
from sqlalchemy.ext.declarative import DeclarativeMeta
from collections import OrderedDict


def asdict(self):
    result = OrderedDict()
    for key in self.__mapper__.c.keys():
        if getattr(self, key) is not None:
            result[key] = str(getattr(self, key))
        else:
            result[key] = getattr(self, key)
    return result


def to_array(all_vendors):
    v = [ asdict(ven) for ven in all_vendors ]
    return jsonify(v)



@app.route('/random_joke', methods=['POST'])
def random_joke():
    f = r"https://api.chucknorris.io/jokes/random"
    data = requests.get(f)
    joke = json.loads(data.text)
    new_joke = Joke(joke["url"], joke["icon_url"], joke["value"])
    db.session.add(new_joke)
    db.session.commit()
    return joke["value"]


@app.route('/saved_jokes', methods=['GET'])
def saved_jokes():
    all_jokes = Joke.query.all()
    return to_array(all_jokes)




if __name__ == '__main__':
    app.run(debug=True, port=5000)
