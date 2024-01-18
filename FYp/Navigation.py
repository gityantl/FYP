#Navigation
"""
Location of plane
Distance with airport
Top 3 nearest airport (distance, fuel, time)
location unit (DMS degrees minutes seconds)
"""

from openap import nav
import os
import pandas as pd
import numpy as np
from openap.extra import aero
import csv
from tabulate import tabulate
from openap import FuelFlow

#include <stdio.h>

#aircraft model
ac='A320'
eng="CFM56-5B4"

#Location of airport (decimal degrees)
airportloc= nav.airport("VHHH")

airport_lat= airportloc["lat"]
airport_lon= airportloc["lon"]

print('Aiport location',airport_lat, airport_lon)

#Current Situation (decimal degrees)
lat= 18.595
lon= 120.545
print('current location',':',lat,lon)


airports = pd.read_csv('P:/FYP/openap-master/openap/data/nav/airports.csv')

df = airports[airports['lat'].between(lat-2, lat+2) & airports['lon'].between(lon-2, lon+2)]

"""
need at least 3 airport
while df.shape[0] < 3:
    n=2
    df = airports[airports['lat'].between(lat-1*n, lat+1*n) & airports['lon'].between(lon-1*n, lon+1*n)]
    n+= 1"""

coords = np.array(df[['lat', 'lon']])
dist2 = np.sum((coords - [lat, lon])**2, axis=1)

#Top 5 airport information
idx = np.array(dist2)
ap = df.iloc[idx, :]
print(ap)

app=np.array(ap)

i=0
print("Distance with current location")
while i<5:
    #calculate distance (km)
    ap_distance= aero.distance(lat, lon,app[i,1], app[i,2])/1000
    
    #calculate time (s)
    ap_time= ap_distance/216*60   #parameter unit km/h
    print(app[i,0],ap_distance,"km", "", ap_time,"mins") #in km
    
    i+=1
    
    #calculate fuel amount (kg/s)
    #climb
"""    if h>100000:
        fuelflow= FuelFlow(ac, eng)
        tas= aero.cas2tas(v_cas, h)   #m/s, m
        fuel_amount= fuelflow.enroute(mass, tas, alt, path_angle=0, fillna=true)  #kg, kt, ft, degrees
        
        #cruise
"""       
        
    
    
    



"""
table format
print(tabulate([['Aditi', 19], ['Anmol', 16], 
				['Bhavya', 19], ['Ananya', 19], 
				['Rajeev', 50], ['Parul', 45]],
			headers=['Name', 'Age']))
"""
