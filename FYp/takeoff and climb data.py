#2 Nov 2023
import os
#import pandas as pd
#import csv                         # read excel
import matplotlib.pyplot as plt    # plot graph
from openap import FlightPhase    # flight phase
#from openap import CruiseOptimizer  # optimal situation for time and fuel (opt)
from openap import nav              # find the location of the waypooint/airport
from openap.traj import Generator        # for gen traj
from openap import WRAP             # kinematic 
from openap import FuelFlow         # fuelflow
from openap import Thrust           # thrust
from openap import aero             # unit in SI unit

#from mpl_toolkits.mplot3d.axes3d import Axes3D     #3D graph
os.environ["PROJ_LIB"] = r"D:\ProgramData\Anaconda3\pkgs\proj4-5.2.0-h6538335_1006\Library\share"; #fixr
from mpl_toolkits.basemap import Basemap

#generate a excel
#DF = pd.DataFrame(data)         
#DF.to_csv(root+'\output.csv',index = False)


#initial every used Class (_init_)
fuel= FuelFlow(ac='A320', eng='CFM56-5B4')
wrap= WRAP(ac='A320')
thrust= Thrust(ac='A320', eng='CFM56-5B4')
phase= FlightPhase()
gen= Generator(ac='A320', eng='CFM56-5B4')


#self no need type in anything
#from HKG to MFM
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
takeoff_fuelflow= fuel.takeoff(tas=80, alt=0)
takeoff_fuelg= fuel.plot_model(plot=True)               #will gen graph auto, no need print

#takeoff_fuelamount= takeoff_fuelflow*takeoff_time
print (takeoff_fuelflow)
#print (takeoff_fuelamount)

#-------------------------------------------------------------------
#gen graph
"Climb"
climb_speed= wrap.initclimb_vcas()
climb_vertical_distance= wrap.climb_range()    #vertical km/s
print(climb_speed, climb_vertical_distance)

"speed"
takeoff_speed= wrap.takeoff_speed()
print (takeoff_speed)

"altitude"


"thrust"


"fuel"



"trag"
gen.enable_noise()
climb_gen=gen.climb()
data_cl = gen.climb(dt=10, cas_const_cl=280, mach_const_cl=0.78, alt_cr=35000)
print(data_cl)

#generating 4 graph for climb trajectories
fig, ax = plt.subplots(2, 2, figsize=(12, 6))
plt.suptitle("Climb trajectories")
for i in range(1):
    #climb situation
    data_cl = gen.climb(dt=10, cas_const_cl=280, mach_const_cl=0.78, alt_cr=35000)
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



data_cl = gen.climb(dt=10, random=True)
data_de = gen.descent(dt=10, cas_const_de=280, mach_const_de=0.78, alt_cr=35000)


data_cr = gen.cruise(dt=60, random=True)

data_all = gen.complete(dt=10, random=True)


#need set data for generating traj but error
#climb_tra= phase.set_trajectory(ts=180, alt=3000, spd=60, roc=70)
#climb_label= phase.phaselabel(twindow=60)
#climb_trajg= phase.plot_logics()

#print(climb_tra,climb_label, climb_trajg)


"nav"
airport_hkg= nav.airport('VHHH')
print(airport_hkg)
#cant get it
print(list(airport_hkg)[1])

lat= 26
lon=120

nextclosest= nav.closest_airport(lat, lon)
print(nextclosest)
sd=nextclosest

if sd =="None":
    print ("yes")
    findfix= nav.closest_fix(lat, lon)
    print(findfix)
    
    




"Graph"
# Earth
for i in range(0,330,20):
    my_map = Basemap(projection='ortho', lat_0=0, lon_0=i, resolution='l', area_thresh=1000.0)
    my_map.bluemarble()
    my_map.etopo()
    name=str(i)
    path='/path/to/your/directory/'+name
    plt.savefig(path+'.png')
    plt.show()
    plt.clf()
    plt.cla()
    plt.close() 
    
