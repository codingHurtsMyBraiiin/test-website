from flask import Blueprint, render_template
from flask import redirect, url_for  #redirecting

views = Blueprint(__name__, "views")   #views is the template name

@views.route("/")
def home():
    return render_template("index.html", name = "Henry")

@views.route("/profile/<username>")   #accessing parameters in an url
def profile(username):
    return render_template("index.html", name = username)

@views.route("/harold")
def harold():
    return render_template("index.html", name = "Harold")

@views.route("/go-home")
def go_home():
    return redirect(url_for("views.home")) #url_for(template_name.route_function)



