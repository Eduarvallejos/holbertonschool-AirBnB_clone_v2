#!/usr/bin/python3
"""
This script lists all objects of the state class
present in the database.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

"""
Close the connection to the database
terminate each Flask application context.
"""


@app.teardown_appcontext
def teardonw_db():
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Gets all objects of the State class from
    the database.
    """
    state_list = storage.all(State).values()
    return render_template("7-states_list.py", states=state_list)


if __name__ == "__main":
    """
    Start the Flask application so that it listens on all
    the interfaces on port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
