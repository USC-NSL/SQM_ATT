import matplotlib
matplotlib.use('Agg')
import glob, os, sys, re, math, operator
import matplotlib.pyplot as plt
import plot_lib
from pylab import *
import numpy as np
import matplotlib.gridspec as gridspec


f_day = -1
f_time = -1
def trans(a):
	global f_day, f_time
	#print a
	for i in range(len(a)):
		t = a[i]
		day = (t % 1000000)/10000
		time = (t % 10000)/100
		if f_day == -1:
			f_day = day
			f_time = time
		a[i] = 24*(day-f_day)+(time-f_time)
	#print a

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

x_ = []
y_ = []
leg = []
for c in [sys.argv[1], sys.argv[2]]:
	f_temp = c
	if not os.path.isfile(f_temp):
		print "error"
		exit()
	data = open(f_temp).readlines()
	t = data[1].split(",")[:-1]
	x = []
	for t_ in t:
		x.append(int(t_))
	trans(x)	

	if len(x) == 0:
		continue

	t = data[3].split(",")[:-1]
	y = []
	leg.append(plot_lib.get_legend("SERVICE_CATEGORY_ID", c))
	for t_ in t:
		y.append(int(t_))
	
	print f_temp
	x, y = add_zero(x, y)
	print x
	print y
	x_.append(x)
	y_.append(y)

	x_tick = range(0, max(x)+24, 24)

aa = []
b = []

for i in range(len(x_[0])):
	t = x_[0][i]
	if not t in x_[1]:
		continue
	i2 = x_[1].index(t)
	aa.append(y_[0][i])
	b.append(y_[1][i2])

fig = plt.figure()
a = sys.argv[1]
enb1 = a[a.find("ENODEB=")+7:a.find(",", a.find("ENODEB="))]
enb1_cat = ""
if a.find("SERVICE_CATEGORY_ID")!= -1:
	enb1_cat = a[a.find("SERVICE_CATEGORY_ID=")+19:a.find(".", a.find("SERVICE_CATEGORY_ID="))]
else:
	enb1 = a[a.find("ENODEB=")+7:a.find(".", a.find("ENODEB="))]
a = sys.argv[2]
enb2 = a[a.find("ENODEB=")+7:a.find(".", a.find("ENODEB="))]

gs = gridspec.GridSpec(2,1,height_ratios=[2,1])
ax = plt.subplot(gs[0])    # The big subplot
ax2 = plt.subplot(gs[1])    # The big subplot

print aa
print b

max_aa = max(aa)
max_b = max(b)

y = {}
for i in range(101):
	y[i] = []
for i in range(len(aa)):
	x = int(aa[i]*100.0/max_aa)
	y[x].append(b[i]*100.0/max_b)
y_avg = []
y_err_1 = []
y_err_2 = []
for i in range(101):
	if y[i] == []:
		y_avg.append(0)
		y_err_1.append(0)
		y_err_2.append(0)
		continue
	avg = average(y[i])
	y_avg.append(avg)
	y_err_1.append(np.percentile(y[i], 85)-avg)
	y_err_2.append((avg-np.percentile(y[i], 15)))

ax.errorbar(range(101), y_avg, yerr=[y_err_2, y_err_1], fmt='x')
#ax.scatter(aa,b, alpha=0.5)
#ax.set_xlim([-0.5, 6.5])
#ax.legend(leg, fontsize=20, ncol=2)
ax.set_xticks([0,20,40,60,80,100])
ax.set_xticklabels(["", "", "", "", "", ""])

ax.set_ylabel("Overall Utilization", fontsize=20)

t = 0
for i in range(101):
	t += len(y[i])
y_p = []
for i in range(101):
	y_p.append(len(y[i])*1.0/t)
ax2.plot(range(101), y_p)
ax2.set_xlim([-1,101])
ax.set_xlim([-1,101])


ax.tick_params(axis='both', which='major', labelsize=18)
ax.tick_params(axis='both', which='minor', labelsize=18)
ax2.tick_params(axis='both', which='major', labelsize=18)
ax2.tick_params(axis='both', which='minor', labelsize=18)

#plt.xticks(x_tick)#, rotation='30')
#plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
ax.grid()
ax2.grid()
ax2.set_xlabel("Streaming Utilization", fontsize=20)
ax2.set_ylabel("Samples", fontsize=20)

fig.savefig("errorbar_%s_vs_%s.png"%(enb1, enb2), bbox_inches='tight')
