#!/usr/bin/python3
"""
This script lists all objects of the state class
present in the database.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Gets all objects of the State class from
    the database.
    """
    state_list = storage.all(State).values()
    # Render the template with the list of states and cities
    return render_template("8-cities_by_states.html",
                           states=state_list)


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
