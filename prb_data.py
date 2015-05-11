import os, sys, glob, operator, time
import lib
# NHPKBSC15

start_date = 7
end_date = 0

def print_entry(s, schema_id):
	t = s.split("|")
	print len(t),len(lib.schemas[schema_id])
	for i in range(len(t)):
		print lib.schemas[schema_id][i][0]+" : "+t[i]+",",
	print ""

def get_filtered(s, f):
	s_ = s.split("|")
	for f_ in f:
		if s_[f_] != f[f_]:
			return []
	return s_

# minutes after 2015-05-start_date
def get_time(s_):
	global start_date, end_date
	d = int(s_[0].split("-")[2]) - start_date
	if d > end_date:
		end_date = d
	s = s_[1][:-1].split(":")
	return d*24*60+int(s[0])*60+int(s[1])

pid = str(os.getpid())
if len(sys.argv) != 4:
	lib.print_usage()
	exit()

data_index = int(sys.argv[1])
filter = {}
t = sys.argv[2].split(",")
for s in t:
	s_ = s.split("=")
	filter[int(s_[0])] = s_[1]
separate = int(sys.argv[3])
print filter

data = {}
for f in glob.glob("*.prb"):
	print "\t", f, 
	ls = open(f).readlines()
	for l in ls:
		l_ = get_filtered(l, filter)
		if l_ != []:
			#print l
			d = float(l_[data_index])*1.0/float(l_[data_index+1])
			ind = ""
			if separate != -1:
				ind = l_[separate]
			if not ind in data:
				data[ind] = {}
			data[ind][get_time(l_)] = d

f_name = str(data_index)+"~"+sys.argv[2]+"_"+sys.argv[3]+"-"+str(start_date)+"-"+str(end_date+start_date)+".out"
f_out = open(f_name, "w")


for se in data:
	lib.printf(f_out, se)
	sorted_data = sorted(data[se].items(), key=operator.itemgetter(0))
	lib.printf(f_out, "Timestamp:")
	s = ""
	for x in sorted_data:
		s += str(x[0]) + ", "
	lib.printf(f_out, s)
	s = ""
	lib.printf(f_out,  str(data_index) + ":")
	for x in sorted_data:
		s += str(x[1]) + ", "
	lib.printf(f_out, s)

f_out.close()
lib.scp_and_plot_prb(f_name)
