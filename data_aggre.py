import os, sys, glob, operator
import lib
# NHPKBSC15

root = "2015_02"
schema_tag = "BA"

def print_entry(s, schema_id):
	t = s.split("|")
	print len(t),len(lib.schemas[schema_id])
	for i in range(len(t)):
		print lib.schemas[schema_id][i][0]+" : "+t[i]+",",
	print ""

pid = str(os.getpid())
if len(sys.argv) != 4:
	lib.print_usage()
	exit()

start_date, end_date = lib.get_date(sys.argv[1])
data_name = sys.argv[2]
filter = lib.get_filter(sys.argv[3], schema_tag)
print filter

timestamp_index = lib.get_index("GMT", schema_tag)
data_index = lib.get_index(data_name, schema_tag)
if data_index == -1:
	print "\t data filed %s invalid"%(data_name)
	exit()

data = {}
for d in range(start_date, end_date + 1):
	folder = root + "/" + lib.get_folder(d)
	files = glob.glob("%s/*RNC*BA*.dat.gz"%(folder))
	print folder, len(files)
	for f in files[:100]:
		lib.get_unzip(f, "temp_%s"%(pid))
		ls = open("temp_%s"%(pid)).readlines()
		for l in ls:
			l_ = lib.get_filtered(l, filter)
			if l_ != []:
				print l
				data[int(l_[timestamp_index])] = l_[data_index]

sorted_data = sorted(data.items(), key=operator.itemgetter(0))
print "\nTimestamp:"
for x in sorted_data:
	print x[0],",",
print "\n" + data_name + ":"
for x in sorted_data:
	print x[1],",",
