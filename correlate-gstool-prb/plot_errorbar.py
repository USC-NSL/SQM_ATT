import matplotlib
matplotlib.use('Agg')
import glob, os, sys, re, math, operator
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from mpltools import color

enb = "HXL05224"
enb = "HXL05368"

top = 15

f_day = -1
f_time = -1
def trans(a):
	global f_day, f_time
	for i in range(len(a)):
		t = a[i]
		day = (t % 1000000)/10000
		time = (t % 10000)/100
		if f_day == -1:
			f_day = day
			f_time = time
		a[i] = 24*(day-f_day)+(time-f_time)

def get_time_from_string(s):
	global f_day, f_time
	t = int(s)
	day = (t % 1000000)/10000
	time = (t % 10000)/100
	return 24*(day-f_day)+(time-f_time)



def add_zero(x, y):
	xx = []
	yy = []

	a = min(x)
	b = max(x)
	for i in range(a, b+1):
		xx.append(i)
		if i in x:
			yy.append(y[x.index(i)])
		else:
			yy.append(0)
	return xx, yy

# 2015-01-08 02:00:00  --->  201501080200
def convert(t):
	return t[0:4] + t[5:7] + t[8:10] + t[11:13] + t[14:16]

f_ = "01_1-5~DL_BYTES~ENODEB=" + enb + ".out"
data = open(f_).readlines()

x_ = []
y_ = []
leg = []
t = data[1].split(",")[:-1]
x = []
for t_ in t:
	x.append(int(t_))
trans(x)	

t = data[3].split(",")[:-1]
y = []
for t_ in t:
	y.append(int(t_))

x, y = add_zero(x, y)
#print x
#print y

data = open("prb.txt").readlines()
NUM = {}
DEN = {}
f_prb = {}
for l in data:
	ls = l.split("|")
	if ls[2] != enb:
		continue
	t = get_time_from_string(convert(ls[1]))
	d = ls[5].split("_")
	for xx in range(len(d)):
		d[xx] = int(d[xx])
	if t in NUM:
		NUM[t] += 5*d[0] + 15*d[1] + 25*d[2] + 35*d[3] + 45*d[4] + 55*d[5] + 65*d[6] + 75*d[7] + 85*d[8] + 100*d[9]
		DEN[t] += d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8] + d[9]
	else:
		NUM[t] = 5*d[0] + 15*d[1] + 25*d[2] + 35*d[3] + 45*d[4] + 55*d[5] + 65*d[6] + 75*d[7] + 85*d[8] + 100*d[9]
		DEN[t] = d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8] + d[9]
#print NUM, DEN
for xx in NUM:
	f_prb[xx] = NUM[xx]*1.0/DEN[xx]
	#print x, f_prb[x]

ii = 0
print x,y
f_x = []
f_y = []
yy = {}
for i in range(101):
	yy[i] = []
for i in range(len(x)):
	if x[i] in f_prb:
		print ii, ":", y[i], f_prb[x[i]]
		ii += 1
		#f_x.append(y[i])
		#f_y.append(f_prb[x[i]])
		p = round(f_prb[x[i]])
		yy[p].append(y[i])

y_avg = []
y_err_1 = []
y_err_2 = []
max_y = -1
for i in range(101):
	if yy[i] == []:
		y_avg.append(0)
		y_err_1.append(0)
		y_err_2.append(0)
		continue
	max_y = i
	avg = average(yy[i])
	y_avg.append(avg)
	y_err_1.append(np.percentile(yy[i], 85)-avg)
	y_err_2.append((avg-np.percentile(yy[i], 15)))


fig = plt.figure()
ax = fig.add_subplot(111)    # The big subplot
#ax.scatter(f_y, f_x)
ax.errorbar(range(101), y_avg, yerr=[y_err_2, y_err_1], fmt='x')

#ax.set_ylim([-1, max(y_t)*1.5])
ax.set_xlim([0, max_y+1])
#ax.legend(leg, fontsize=10, ncol=3)
ax.set_xlabel("PRB utilization", fontsize=20)
ax.set_ylabel("Downlink Bytes", fontsize=20)
ax.set_title(enb, fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
#plt.xticks(x_tick)#, rotation='30')
plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("traffic_vs_prb_errorbar_%s.png"%(enb), bbox_inches='tight')
