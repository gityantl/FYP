"""
Trajectory

rate of climb = vertical rate

1 knot = 1.852 km
1 m/s = 3.6 km/h

takeoff 0ft-50ft (0-35ft)
initial climb (35-1500ft)
climb (10k-50k)
cruise (For A320, max= )
Final aproach (last 1000ft)
landing (alt=0)

"""
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
import matplotlib.pyplot as plt

#aircraft model
ac='A320'
eng="CFM56-5B4"

#Class
phase= FlightPhase()
wrap= WRAP(ac)
gen= Generator(ac,eng)
thrust= Thrust

#set_Trajectory
noise_allow= gen.enable_noise()

#parameter
#climb
cas_const_cl= wrap.climb_const_vcas()["default"]*1.943844
mach_const_cl= wrap.climb_const_mach()["default"]
print(cas_const_cl, mach_const_cl)

#descent
cas_const_de=wrap.descent_const_vcas()["default"]*1.943844
mach_const_de=wrap.descent_const_mach()["default"]
print(cas_const_de,mach_const_de)


#get trajectory data
cl_data= gen.climb(dt=10, cas_const_cl=cas_const_cl , mach_const_cl=mach_const_cl, alt_cr=50000)  #unit (s, kt, , ft)
#print(cl_data)


for cas_const_de in np.arange (cas_const_de,0,20.45):
    print(cas_const_de)
    de_data= gen.descent(dt=10,cas_const_de=cas_const_de ,mach_const_de=mach_const_de,alt_cr=50000)
    print(de_data)
    
    fig, ax = plt.subplots(1, figsize=(12, 6))
    plt.suptitle("Descent trajectories")
    pt= ax.plot(de_data["t"], de_data["h"] / aero.ft, label="%d/%.2f" % (de_data["cas_const_de"], de_data["mach_const_de"]),)
    plt.show()


#plot graph
fig, ax = plt.subplots(1, figsize=(12, 6))
plt.suptitle("Climb trajectories")
pt= ax.plot(cl_data["t"], cl_data["h"] / aero.ft, label="%d/%.2f" % (cl_data["cas_const_cl"], cl_data["mach_const_cl"]),)
plt.show()
