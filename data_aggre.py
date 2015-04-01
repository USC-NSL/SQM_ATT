import os, sys, glob, operator
import lib
# NHPKBSC15

root = "2015_02"
schema_tag = "RNC_BA"

def print_entry(s, schema_id):
	t = s.split("|")
	print len(t),len(lib.schemas[schema_id])
	for i in range(len(t)):
		print lib.schemas[schema_id][i][0]+" : "+t[i]+",",
	print ""

pid = str(os.getpid())
if len(sys.argv) != 5:
	lib.print_usage()
	exit()

schema_tag = sys.argv[1]
schema_tags = schema_tag.split("_")
start_date, end_date = lib.get_date(sys.argv[2])
data_name = sys.argv[3]
filter = lib.get_filter(sys.argv[4], schema_tag)
print filter

f_name = sys.argv[2]+"~"+data_name+"~"+sys.argv[4]+".out"
f_out = open(f_name, "w")

timestamp_index = lib.get_index("GMT", schema_tag)
data_index = lib.get_index(data_name, schema_tag)
if data_index == -1:
	print "\t data filed %s invalid"%(data_name)
	exit()

data = {}
for d in range(start_date, end_date + 1):
	folder = root + "/" + lib.get_folder(d)
	files = glob.glob("%s/*%s*%s*.dat.gz"%(folder, schema_tags[0], schema_tags[1]))
	print folder, len(files)
	for f in files:
		lib.get_unzip(f, "temp_%s"%(pid))
		ls = open("temp_%s"%(pid)).readlines()
		for l in ls:
			l_ = lib.get_filtered(l, filter)
			if l_ != []:
				#print l
				if int(l_[timestamp_index]) in data:
					data[int(l_[timestamp_index])] += int(l_[data_index])
				else:
					data[int(l_[timestamp_index])] = int(l_[data_index])

sorted_data = sorted(data.items(), key=operator.itemgetter(0))
lib.printf(f_out, "Timestamp:")
s = ""
for x in sorted_data:
	s += str(x[0]) + ", "
lib.printf(f_out, s)
s = ""
lib.printf(f_out,  data_name + ":")
for x in sorted_data:
	s += str(x[1]) + ", "
lib.printf(f_out, s)

os.system("rm temp_%s"%(pid))

f_out.close()
lib.scp_and_plot(f_name)
