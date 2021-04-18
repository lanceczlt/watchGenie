from flask import Blueprint, render_template, request, flash, jsonify, session
import numpy as np 
import pandas as pd 
import scipy.optimize 
from .db_connection import connect

connect, cursor = connect()
recommend = Blueprint('recommend', __name__)

@recommend.route('/recommend', methods=['GET','POST'])
def recommend():
    if request.method == 'POST':
        return render_template("recommendation.html")         
    return render_template("recommendation.html")

# given a list of genres and a language, return the top movies
# for the registration user interest learning process
def getTopMovies(genres, language):
    return None

def content_based_rec():
    return None

def plot_based_rec():
    return None

def collaboration_based_rec():
    return None



