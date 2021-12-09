# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:19:18 2021

@author: HP
"""

import numpy as np
t=np.arange(12,480,12)
#print(len(t))
print("time in hrs",t)
t1=12*3600
#print(t1)
infl=np.array([370,1250,3400,5750,7220,7400,6730,4560,3200,2450,1920,1440,1180,950
       ,800,670,560,500,420,370,1250,3400,5750,7220,7400,6730,4560,3200,2450,
       1920,1440,1180,950,800,670,560,500,420])
#print(len(infl))
#print(len(infl))
outfl=np.array([370,520,1300,2870,4720,5240,6760,6380,5740,3940,3070,2350,
        1800,1420,1140,930,770,640,550,370,520,1300,2870,4720,6240,6760,
        6380,5740,3940,3070,2350,1800,1420,1140,930,770,640,550])

volinf = np.zeros_like(infl)
 

for i in range(1,38):
    volinf[i] =(((infl [i] +infl[i-1])/2 )*t1)/10**6 
print("volume of inflow",volinf)
volouf= np.zeros_like(outfl)
#for i in range(1,38):
for i in range(1,38):
    volouf[i] =(((outfl [i] +outfl[i-1])/2 )*t1)/10**6 
print("volume of outflow",volouf)
sto=0
sto=volinf-volouf
print("storage",sto)
print("successive storage",sto)
cumsto = np.zeros_like(sto)
#volsto=0
for i in range(1,19):
    #cumsto[i] =(sto [i] +sto[i-1])
    cumsto[i+1]=cumsto[i]+sto[i]
print("cumulative storage",cumsto) 
cumsto1=[0, 15,76,183,300,400,446, 406,312, 225, 168,]


x=0.2
a=infl*x+(1-x)*outfl

print("a=",a) 
a1=[370, 666,1720, 3446, 5220,5672, 6754, 6016,5232, 3642, 2840]
import matplotlib.pyplot as plt

x=0.3
b=infl*x+(1-x)*outfl
print("b",b)
b1=[370,739, 1930, 3734, 5470, 5888,6751, 4978, 3493, 2725,2077]
fig = plt.figure(figsize=(8, 6))

line1, = plt.plot(cumsto1, a1, label=' storage-a1')
line2, = plt.plot(cumsto1, b1, label='storage-b1')
plt.legend(handles=[line1, line2], loc='best')
plt.minorticks_on()
plt.grid(b=True, color='aqua', alpha=0.6, linestyle='dashdot')
fig.suptitle('"Storage vrs [xI+(1-x)O] "', fontsize=12)
plt.xlabel('Storage', fontsize=10)
plt.ylabel('[xI+(1-x)O] for x=0.2', fontsize=10)
#plt.title("Storage vrs [xI+(1-x)O] for x=0.2")
plt.show()
stor1=np.array([183,300,400]) 
x1=np.array([3446, 5220,5672])

#storage=(160100)*10**6
x=(3200-2200)/(24*3600)
k=((160-100)*10**6/(3200-2200)/(24*3600))
#k1=print((160-100)*10**6/(3200-2200)/(24*3600)) 
print("k",round(k,3))
