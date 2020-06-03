
# Simulation of a medical sensor

__Step 1: simulate the medical sensor__

In the first step we can simulate a medical sensor reading a patient's parameter using the class Sensor in simulate_sensor.py. Every Sensor object can be started as a thread and once started will produce data every 5 seconds and save it to .csv every minute. 
The script patients.py has functions to start threads given a patient ID and to save all the data from the IDs in a pandas dataframe.

TODO: Write a method in Sensor that pushes the data to the API instead of saving it in .csv


__Step 3: simulate the API__

Simulate a API with simulate_API.py to obtain the data from Step 1 and start/stop different patient threads.

TODO: Make sure that the data is deleted every time it is sent to the API.


__Step 4: simulate a request for the API__

Using simulate_request.py we can retrieve the data from the API and save them in a csv file.

__To test the API__

Download the mock data and in the same directory run:

$ python3 simulte_API.py 1 2 3

and in another terminal:

$ python3 simulate_request.py
