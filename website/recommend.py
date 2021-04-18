from flask import Blueprint, render_template, request, flash, jsonify, session
import numpy as np 
import pandas as pd 
import scipy.optimize 

recommend = Blueprint('recommend', __name__)

@recommend.route('/recommend', methods=['GET','POST'])
def getRecommendations():
    if request.method == 'POST':
        return render_template("recommendation.html", user = current_user)         
    return render_template("recommendation.html", user = current_user)
