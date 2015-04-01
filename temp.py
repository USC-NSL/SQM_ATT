import os

ls = open("field.txt")

for l in ls:
	print "(\""+l[:l.find(" ")]+"\",\""+l[l.find(" ")+1:-1]+"\"), ",
