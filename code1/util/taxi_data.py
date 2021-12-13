import pandas as pd
import random

t = " 12/21/2015 03:00:00 PM"


cols = ['Taxi ID', 'Trip Start Timestamp',
        'Trip Seconds', 'Trip Miles', 'Fare',
        'Pickup Centroid Latitude',
        'Pickup Centroid Longitude',
        'Dropoff Centroid Latitude',
        'Dropoff Centroid Longitude']

file = pd.read_csv('F:/data_file/Taxi_Trips(example).csv', usecols=cols, nrows=10)
var = file['Trip Start Timestamp']

print(var)
