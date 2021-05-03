from flask import Blueprint, render_template, request, flash, jsonify, session
from db_connection import connect
import numpy as np 
import pandas as pd 
import scipy.optimize 

