# -*- coding: utf-8 -*-

#set all variables, also calculate some values
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#print out those calculated values
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There wil be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "hey %s there." % "you"
tmpname="bian"
print 'hey %s there.' %tmpname
