import os
import numpy as np
import skfuzzy as fuzz
import csv                                # read excel
import matplotlib.pyplot as plt            # plot graph
from openap import FlightPhase             # flight phase
#from openap import CruiseOptimizer        # optimal situation for time and fuel (opt)
from openap import nav                     # find the location of the waypooint/airport
from openap.traj import Generator          # for gen traj
from openap import WRAP                    # kinematic 
from openap import FuelFlow                # fuelflow
from openap import Thrust                  # thrust
from openap import aero                    # unit in SI unit
from math import sin, cos, sqrt, atan2

"""unit
1 knot = 1.852 km/h
"""

#initial every used Class (_init_)

fuel= FuelFlow(ac='A320', eng='CFM56-5B4')
wrap= WRAP(ac='A320')
thrust= Thrust(ac='A320', eng='CFM56-5B4')
phase= FlightPhase()
gen= Generator(ac='A320', eng='CFM56-5B4')

#takeoff 0ft-50ft (0-35ft)
#speed & change
print('Takeoff phase')

takeoffspeed= wrap.takeoff_speed()["default"]
print('takeoff speed',takeoffspeed,'m/s')

fuel_rate= fuel.takeoff(tas=takeoffspeed*1.94384449, alt=0, throttle=1) #knot, ft, 0-1 (1 full thrust)
print('fuel rate',fuel_rate,'kg/s')

fuel_rate= fuel.takeoff(tas=takeoffspeed*1.94384449, alt=50, throttle=1)
print('fuel rate',fuel_rate,'kg/s')

takeoffdistance= wrap.takeoff_distance()["default"]
print('take off distance',takeoffdistance,'km')

takeofftime= (takeoffdistance*1000)/takeoffspeed
print('takeoff time',takeofftime,'s')

Total_fuel_amount_takeoff = takeofftime*fuel_rate
print('total amuont of fuel needed',Total_fuel_amount_takeoff, 'kg')

# intial climb (35-15kft) (15-454.5m)
print('Initial climb phase')
climb_cas= wrap.initclimb_vcas()["default"]
print('Climb CAS',climb_cas, 'km/s')

# climb (10k-50k)

#generating 4 graph for climb trajectories
fig, ax = plt.subplots(2, 2, figsize=(12, 6))
plt.suptitle("Climb trajectories")
for i in range(1):
    #climb situation
    data_cl = gen.climb(dt=10, cas_const_cl= 280, mach_const_cl=0.78, alt_cr=35000)
    #graph 1
    ax[0][0].plot(
        data_cl["t"],
        data_cl["h"] / aero.ft,
        label="%d/%.2f" % (data_cl["cas_const_cl"], data_cl["mach_const_cl"]),
    )
    ax[0][0].set_ylabel("Altitude (ft)")
    #graph 2
    ax[0][1].plot(data_cl["t"], data_cl["s"] / 1000)
    ax[0][1].set_ylabel("Distanse (km)")
    #graph 3
    ax[1][0].plot(data_cl["t"], data_cl["v"] / aero.kts)
    ax[1][0].set_ylabel("True airspeed (kt)")
    #graph 4
    ax[1][1].plot(data_cl["t"], data_cl["vs"] / aero.fpm)
    ax[1][1].set_ylabel("Vertical rate (ft/min)")
    #label position
    ax[0][0].legend()
plt.show()

# cruise (For A320, max= )

# descent ()

# Final aproach (last 1000ft)

#landing (alt=0)




  







