import os
f = open("temp").readlines()

for x in f:
	print "\"", x[:-1],"\"",
