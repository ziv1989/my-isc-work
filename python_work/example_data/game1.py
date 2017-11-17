#!/bin/env python2.7

location= "/home/user01/my-isc-work/python_work/example_data/weather.csv"

import numpy as np

a= np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1,2.1,21,1.1,-2]])

temp=[]
with open(location, "r") as reader:
    reader.readline()
    for line in reader.readlines():
	t=line.split(",")[2]
	t=float(t)
	temp.append(t)

print temp


#def double_it(number):
#    return 2 * number

nox = [10.45345, 200.42342, 30]

count = 0
while count < len(nox):
    item = nox[count] / temp[count]
    
    count += 1ls
    if item < 20:
	print "low, {0:8.3f} ".format(item)
    elif item >= 20:
	print "high,{0:8.3f} ".format(item)

#plot an array! and temp/co2/no2 seperately

import matplotlib.pyplot as plt
x = np.arange(10)

#plt.plot(x*3)
#plt.show()

fig,ax1 = plt.subplots()

temp = [14.1,15.5,16.4,14.6,14.4,17.3,20.1]
times = range(7)
co2 = [250,265,272,260,300,320,389]

ax1.plot(times,co2,"b--")
ax1.set_ylabel("[CO2]")
ax2 = ax1.twinx()
ax2.plot(times,temp, "r*-")
ax2.set_ylabel("temp (C)")

plt.show()

#

#print double_it(nox)

#nox = range(5)
#return nox*2
#if nox > 3:
   # print "high"
	#elif nox < 3:
          #  print low
