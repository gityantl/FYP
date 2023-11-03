#1 Nov 2023


from openap import WRAP

wrap= WRAP('A320')
sd=WRAP.takeoff_speed(wrap)
print (sd)

wrap= WRAP('A319')
sd=WRAP.takeoff_speed(wrap)
print (sd)


wrap= WRAP('A320')
sd=WRAP.landing_distance(wrap)
print (sd)


