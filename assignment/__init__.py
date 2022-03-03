from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
'''
Pandas was used to pass the csv file at the flask app initialization stage.
The parsed csv file is then sent to routes.py for routing
'''
listed_companies = pd.read_csv('SalaryDataset.csv')
from assignment import routes