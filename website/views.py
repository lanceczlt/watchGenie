from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for, session
import json
import pandas as pd 
import numpy as np 
from .db_connection import connect

views = Blueprint('views', __name__)
connect, cursor = connect()


@views.route('/', methods=['GET', 'POST'])
def landing():
    return render_template("landing.html")

@views.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("search.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return None
    else:
        return render_template("search_result.html")


