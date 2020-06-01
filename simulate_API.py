"""
Simulates an API to get medical data of a list of patients in a time
interval.
"""
import flask
import json
import sys
import pandas as pd
from datetime import datetime, timedelta
from flask import request, jsonify
from simulate_sensor import Sensor
from patients import get_patient_list

# Read in the IDs list
IDs = sys.argv[1:]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# TODO: Get the data for the patients in IDs in
# a given time frame interval
readable_sensor = get_patient_list(IDs)
data_json = pd.DataFrame.to_json(readable_sensor)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Cosinuss Sensor</h1>
<p>A prototype API to recieve and downloar Cosinuss sensor data.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/data', methods=['GET'])
def api_all():
    return jsonify(data_json)

app.run()
