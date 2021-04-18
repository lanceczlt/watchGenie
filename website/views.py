from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for, session
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('auth.login'))