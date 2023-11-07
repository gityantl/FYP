#2 Nov 2023
#import pandas as pd
#import csv                       # read excel
#import matplotlib.pyplot as plt  # plot graph
#from openap import FlightPhase   # flight phase
from openap import WRAP          # kinematic 
from openap import FuelFlow      # fuelflow
from openap import Thrust        # thrust

#generate a excel
#DF = pd.DataFrame(data)         
#DF.to_csv(root+'\output.csv',index = False)

#initial (_init_)
fuel= FuelFlow(ac='A320', eng='CFM56-5B4')
wrap= WRAP(ac='A320')
thrust= Thrust(ac='A320', eng='CFM56-5B4')

"takeoff"

"speed"
takeoff_speed= wrap.takeoff_speed()
print (takeoff_speed)

"takeoff distance"
takeoff_distance= wrap.takeoff_distance()
print (takeoff_distance)

"time needed for takeoff"

#takeoff_time= takeoff_distance/takeoff_speed

"thrust"
takeoff_thrust= thrust.takeoff(tas=70,alt=0)
print (takeoff_thrust)

"drag"


"fuel"
takeoff_fuelflow= fuel.takeoff(tas=70, alt=0)
#takeoff_fuelamount= takeoff_fuelflow*takeoff_time
print (takeoff_fuelflow)
#print (takeoff_fuelamount)

#-----------------------------------------------------------
#gen graph

"initclimb"
initclimb_speed= wrap.initclimb_vcas()
initclimb_rate= wrap.initclimb_vs()
print(initclimb_speed, initclimb_rate)

"Climb"
climb_speed= wrap.climb_const_vcas()
climb_vertical_distance= wrap.climb_range()    #vertical km/s
print(climb_speed, climb_vertical_distance)

"speed"

"altitude"

"thrust"

"fuel"








"problem: how to determine the value, tas, self cal? or hv database"
