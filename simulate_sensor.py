"""
Class to simulate a patient's medical parameters in a given timne interval.
"""
# import bluetooth
import numpy as np
import pandas as pd
import random
import threading
import time
import datetime
import json
import os

# TODO: Add details of the hospitals in which the patient using the
# sensor can be found.


class Sensor(threading.Thread):
    """Class to simulate a sensor"""

    def __init__(self, ID, s=1):
        """The constructor returns the istant patient's parameter.
        Randomly draw the patient parameters from a normal
        distribution  in the time interval of length s seconds.
        Input:
        ------
        s: a time interval in seconds, default = 1
        Output:
        -------
        object of type Sensors with parameters ID (sensor Id), HB
        (heart beat [bpm]), O2 (Oxigen concentration [%]), Pd
        (diastolic pressure [mmHg]), Ps (systolic pressure [mmHg]),
        T (temperature [C])
        """
        # TODO: I guess these will be read via BLE?

        threading.Thread.__init__(self)
        self.ID = ID
        self.HB = list(np.random.normal(80, 0.5, s))
        self.O2 = list(np.random.normal(97, 0.1, s))
        self.Pd = list(np.random.normal(80, 0.3, s))
        self.Ps = list(np.random.normal(120, 0.1, s))
        self.T = list(np.random.normal(36.5, 0.1, s))
        self.readable = pd.DataFrame()
        self._is_running = True
        # self.start()

    def get_patient(self, T, interval=False):
        """Get the parameter of the patient with sensor Id ID
        in the specified time interval. If no time interval is given
        it returns the patient's parameters that istant.
        """
        dict_sensor = dict([('ID', self.ID), ('Time', T),
                          ('HB [bpm]', self.HB), ('O2 levels [%]',
                          self.O2), ('P systolic', self.Ps),
                          ('P diastolic', self.Pd), ('T [C]',
                          self.T)])

        db_sensor = pd.DataFrame(dict_sensor)
        db_sensor = db_sensor.set_index('Time')
        self.readable = pd.concat([self.readable, db_sensor])

    def save_data(self):
        """Save the dictionary of data to csv. Every time the data is saved
        clear self.readable
        """
        # TODO: send to API instead of saving it to csv
        if os.path.isfile(self.ID+'.csv'):
            self.readable.to_csv(self.ID+'.csv', mode='a', header=False)
        else:
            self.readable.to_csv(self.ID+'.csv', mode='a')
        self.readable = pd.DataFrame()

    def run(self, save=True):
        """Return a new set of data every 10 second, dump them in a .csv
        file every minute if save = True
        """
        countdown = 0
        while(self._is_running):
            time.sleep(5.)
            countdown += 1
            self.get_patient(time.strftime("%H:%M:%S", time.localtime()))
            if countdown%12 == 0 and save:
                self.save_data()

    def stop(self):
        """Stops the thread by changing _is_running value to False
        """
        self._is_running = False
        print('Patent '+self.ID+' thread stopped')
