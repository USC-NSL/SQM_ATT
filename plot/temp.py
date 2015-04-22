import os
f = open("temp").readlines()

for x in f:
	t = x[:-1].split(" ")
	print "\"", t[1],"\":", t[0], ",",
