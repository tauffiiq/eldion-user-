from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route("/perawat")
@login_required
def perawat():
    return render_template("perawat.html", user=current_user)

@views.route("/fisio")
@login_required
def fisio():
    return render_template("fisio.html", user=current_user)

@views.route("/layanan")
def layanan():
    return render_template("layanan.html", user=current_user)

@views.route("/regist")
def regist():
    return render_template("regist.html", user=current_user)

@views.route("/bio")
@login_required
def biodata():
    return render_template("bio.html", user=current_user)

@views.route("/pay")
def payment():
    return render_template("pay.html", user=current_user)
