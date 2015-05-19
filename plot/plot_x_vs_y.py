import matplotlib
matplotlib.use('Agg')
import glob, os, sys, re, math, operator
import matplotlib.pyplot as plt
import plot_lib
from pylab import *

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
grid()
a = sys.argv[1]
enb1 = a[a.find("ENODEB=")+7:a.find(",", a.find("ENODEB="))]
a = sys.argv[2]
enb2 = a[a.find("ENODEB=")+7:a.find(".", a.find("ENODEB="))]
ax = fig.add_subplot(111)    # The big subplot
ax.scatter(aa,b, alpha=0.5)
#ax.set_xlim([-0.5, 6.5])
#ax.legend(leg, fontsize=20, ncol=2)
ax.set_xlabel("Streaming Traffic of " +enb1, fontsize=20)
ax.set_ylabel("Total Traffic of "+enb2, fontsize=20)
ax.set_title(enb1 + " vs. " + enb2, fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
#plt.xticks(x_tick)#, rotation='30')
#plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("x_vs_y.png", bbox_inches='tight')
