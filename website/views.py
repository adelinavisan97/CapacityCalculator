from flask import Blueprint, render_template
from website.myfile import *

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", text1=rowOne[0], text2=rowOne[1], text3=rowOne[2])


print(one[0])
