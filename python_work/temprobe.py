#!/bin/env python2.7
import serial
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE)

data = float(ser.read(size=8).strip()[1:6])
print dt.datetime.utcnow().isoformat(),str(data)

j=0
temp_temp=[]
time_list=[]

while j<20:
    data = float(ser.read(size=8).strip()[1:6])
    time = dt.datetime.utcnow()
    print time ,str(data)
    temp_temp.append(data)
    time_list.append(time)
    j+=1     

new_times = matplotlib.dates.date2num(time_list)


plt.plot_date(new_times,temp_temp,'r--')
plt.xlabel('Time')
plt.ylabel('Temperature in degrees')
plt.gcf().autofmt_xdate()
plt.show()


