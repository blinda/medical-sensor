"""
Simulates an API request. The user needs to run simulate_API.py before
to simulate the webpage.
"""
import base64
import zlib
import pandas as pd
import requests
from flask import jsonify
import json

# Read byte content
coded = requests.get('http://127.0.0.1:5000/api/data')

# Decode from base64
res = base64.b64decode(coded.text)
# Decompress bytes
res_exp = zlib.decompress(res)
# Decode to utf-8
res_str = res_exp.decode()
# Convert to json
r = json.loads(res_str)

df = pd.DataFrame(r)

# Save as csv
df = df.set_index('ID')
df = df.sort_index()
df.to_csv("Patient.csv")
