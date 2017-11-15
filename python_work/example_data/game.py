location= "/home/user01/my-isc-work/python_work/example_data/weather.csv"
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

#print double_it(nox)

#nox = range(5)
#return nox*2
#if nox > 3:
   # print "high"
	#elif nox < 3:
          #  print low
