import pandas as pd
import random

file = pd.read_csv('F:/data_file/Taxi_Trips(example).csv',
                   usecols=['Taxi ID', 'Trip Seconds', 'Trip Miles', 'Fare',
                            'Pickup Centroid Latitude', 'Pickup Centroid Longitude', 'Dropoff Centroid Latitude',
                            'Dropoff Centroid Longitude'],
                   )

m_dict = {}

text_id = []
trip_seconds = []
fare = []
latitude = []
longitude = []
credit = []

print(file.loc[0])
for i in range(len(file)):
    tmp = file.loc[i]
    if tmp['Taxi ID'] not in m_dict:
        m_dict[tmp['Taxi ID']] = 1
        if (41.875750 <= tmp['Pickup Centroid Latitude'] <= 41.88778) and \
                (-87.636954 <= tmp['Pickup Centroid Longitude'] <= -87.616353):
            if (41.875750 <= tmp['Dropoff Centroid Latitude'] <= 41.88778) and \
                    (-87.636954 <= tmp['Dropoff Centroid Longitude'] <= -87.616353):
                text_id.append(tmp['Taxi ID'])
                trip_seconds.append(tmp['Trip Seconds'])
                fare.append(str(tmp['Fare']).replace('$', ''))
                latitude.append(tmp['Pickup Centroid Latitude'])
                longitude.append(tmp['Pickup Centroid Longitude'])
                credit.append(round(random.uniform(0.4, 0.8), 3))
    else:
        m_dict[tmp['Taxi ID']] += 1

df = pd.DataFrame(
    {'Trip Seconds': trip_seconds, 'Fare': fare, 'Latitude': latitude, 'Longitude': longitude, 'credit': credit})

df.to_csv('User.csv', header=True, index=True, sep=',')
print(len(df))
