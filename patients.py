"""
Create a list of patients with medical parameters given by the class
Sensor.
"""
import zlib
import base64
import json
import pandas as pd
from simulate_sensor import Sensor


def initiate_patient(ID):
    """Starts thread of patient with sensor Id ID
    in the specified time interval.
    """
    patient = Sensor(ID)
    patient.start()
    return patient


def stop_patient(patient):
    """Stops thread of patient with sensor Id ID
    in the specified time interval.
    """
    # TODO: get it by id?
    patient.stop()


def initiate_patient_list(listID):
    """Starts thread of patients with sensor Id ID
    in the list. Returns dictionary of patients.
    """
    patient_dict = {}
    for ID in listID:
        patient_dict[ID] = initiate_patient(ID)
    return patient_dict


def stop_patient_list(patient_dict):
    """Stops thread of patient with sensor Id ID
    in the list.
    """
    for ID in patient_dict:
        stop_patient(patient_dict[ID])


def get_one_patient(ID):
    """Get the parameter of the patient with sensor Id ID
    in the specified time interval. If no time interval is given
    it returns the patient's parameters that istant.
    """

    # Create istance of type Sensor in the given time interval
    # (if specified)

    try:
        readable_sensor = pd.read_csv(ID+'.csv')
        readable_sensor.set_index('ID')
        # os.remove(ID+'.csv')
    except FileNotFoundError:
        print('No file found for patient no. '+ID)

    return readable_sensor


def get_patient_list(IDs):
    """ Returns the parameters for a list of patients in base64.
    """
    # TODO: read only data in a specified time interval
    # TODO: remove csv file once it is read
    readable_sensors = pd.DataFrame()
    # Create some test data for our catalog in the form of a pandas df
    for i, ID in enumerate(IDs):
        sensor = get_one_patient(ID)
        readable_sensors = pd.concat([readable_sensors, sensor])
    # Set the ID of the sensor as index of the DataFrame
    readable_sensors.reset_index(drop=True, inplace=True)
    data_json = pd.DataFrame.to_json(readable_sensors)
    # Encode it as bytes object
    enc = data_json.encode()  # utf-8 by default
    # Compress
    comp = zlib.compress(enc)
    # Shrink to base64
    return base64.b64encode(comp)


def check_patient(patient_list, ID):
    """Check the parameters of a patient in patient_list
    with sensor ID"""

    for patient in patient_list:
        if patient.ID == ID:
            return patient
        else:
            return 'ID {} not found'.format(ID)
