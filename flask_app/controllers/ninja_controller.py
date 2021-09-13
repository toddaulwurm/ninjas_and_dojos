from flask_app import app
from flask import render_template, redirect, session, request 

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("ninja.html", dojos = dojos)

@app.route("/new_ninja")
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/create_ninja", methods=['POST'])
def create_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id'],
    }
    Ninja.create_ninja(data)
    return redirect("/dojos")

