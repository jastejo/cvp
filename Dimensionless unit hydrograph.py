# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:35:49 2024

@author: Prasad
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.array([0,6,12,18,24,27,30,36,42,48,54,60,66,72,78,84,90]) 
print(len(t))
print(t[3])
q=np.array([0.0,13.20,41.60,83.20,247.20,263.0,204.60,123.80,74.90,45.20,27.40,16.60,10.10,6.10,
     3.60,2.10,0.00 ]) 
print(len(q))
#plt.plot(t,q)
#print (q[3])
#print(q[2])
#
lg1=t*q
print("lg1",lg1)
lag=np.sum(lg1)
print("lag",lag)
#print(lag)
qsum=np.sum(q)
print("qsum",qsum)
lag=np.divide(lag,qsum)
print("lag=",lag)
# lag +semiduration is lgs
# catchment area (ca) is 1950 sqkm
ca=1950
#volume of runoff(vrf) from 1cm rainfall over a catchment area of 1950 sqkm
vrf=np.divide((1950*10**6),(100*3600*24))
print("vrf",vrf)
# (lag +semiduration)/volume is lgsv
lgsv=np.divide(lag,vrf)
#((lag+semiduration)/volume is lgsv
#lgsv=0.1413 as comuted im mutreja
print("lgsv=",lgsv)

#ordinates of dimensionless hydrograph is oddh
oddh= np.multiply(lgsv,q)
print("ordinates of dimensionless hydrograph",np.round(oddh,2))
#Absissa (x values) is reprsented abs
abs=np.divide((t*100),lag)
print("Absissa",np.round(abs,2))
oddhd=np.array([0,1.76,5.56, 11.12, 33.03, 35.14, 27.34, 16.54, 10.01,  6.04,  3.66,  2.22, 1.35,  0.82,  0.48,  0.28, 0  ])
abs=np.array ([0, 19.9 , 39.79, 59.69, 79.59, 89.54, 99.48,119.38,139.28,159.18, 179.07, 198.97, 218.87, 238.76, 258.66, 278.56, 298.45])
plt.plot(abs,oddhd)
plt.xlabel("Time as Percentage of(Lag+Semi Duration)")
plt.ylabel("Discharge*((lag+semi Duration in hrs)/(Runoff voloume)")
#plt.legend(loc="upper right")
plt.title("Dimensionless unit Hydrograph")

#plt.plot(a, b, "-b", label="sine")
#plt.plot(x, y2, "-r", label="cosine")
#plt.legend(loc="upper right")
#plt.blim(-1.5, 2.0)
plt.show()



