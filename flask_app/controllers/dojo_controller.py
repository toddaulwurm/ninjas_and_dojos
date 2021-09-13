from flask_app import app
from flask import render_template, redirect, session, request 

from flask_app.models.dojo import Dojo

@app.route("/new_dojo", methods=["POST"])
def new_dojo():
    data = {
        "name" : request.form["name"],
    }
    Dojo.create_dojo(data)

    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def dojo_ninjas(id):

    data = {
        "dojo_id" : id,
    }
    dojo = Dojo.dojo_ninjas(data)
    return render_template("dojo_ninjas.html", dojo = dojo)

