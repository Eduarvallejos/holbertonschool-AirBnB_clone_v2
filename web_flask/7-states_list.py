#!/usr/bin/python3
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardonw_db():
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    state_list = storage.all(State).values()
    return render_template("7-states_list.py", states=state_list)


if __name__ == "__main":
    app.run(host="0.0.0.0", port=5000)
