from flask import Blueprint, render_template
from website.myfile import *

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", boolean=False)


@auth.route('/logout')
def logout():
    return render_template("login.html", text=rowOne)


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
