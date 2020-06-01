"""
Simulates an API request. The user needs to run simulate_API.py before
to simulate the webpage.
"""
import pandas as pd
import requests
from flask import jsonify
import json

res = requests.get('http://127.0.0.1:5000/api/data')
r = json.loads(res.text)
print(r)

df = pd.read_json(r)

df = df.set_index('ID')
df = df.sort_index()
df.to_csv("Patient.csv")
