#!/usr/bin/python3
"""
This script lists all objects of the state class
present in the database.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    if id:
        """Gets the State object corresponding to the ID"""
        state_id = storage.get(State, id)
        return render_template("9_states.html",
                               states=state_id)
    else:
        """If no ID is provided, get the list of all states"""
        state_list = storage.all(State).values()
        return render_template('9_states.html', states=state_list)


@app.teardown_appcontext
def teardonw_db():
    """
    Close the connection to the database
    terminate each Flask application context.
    """
    storage.close()


if __name__ == "__main__":
    """
    Start the Flask application so that it listens on all
    the interfaces on port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
