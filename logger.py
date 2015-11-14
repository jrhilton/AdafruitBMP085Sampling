#!/usr/bin/python
# -*- coding: utf-8 -*-

import Adafruit_BMP.BMP085 as BMP085
import time

sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

# read pressure and convert from pa to hpa
#p = sensor.read_pressure()
#p = p / 100.00

#read temperature
#t = sensor.read_temperature()

# we can also build lists, first start with an empty one
elements_p = []

# then use the range function to do 0 to 5 counts
for i in range(0, 60):
    p = sensor.read_pressure()
    p = p / 100.00
    print "Adding %s to the list." % p
    # append is a function that lists understand
    # time.sleep(1)
    # print p
    elements_p.append(p)


elements_t = []

# then use the range function to do 0 to 5 counts
for i in range(0, 60):
    t = sensor.read_temperature()
    print "Adding %s to the list." % t
    # append is a function that lists understand
    # time.sleep(1)
    # print p
    elements_t.append(t)



# now we can print them out too
#for i in elements:
 #   print "Element was: %d" % i


print sum(elements_p) / float(len(elements_p))
print sum(elements_t) / float(len(elements_t))



