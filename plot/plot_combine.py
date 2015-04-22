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

f_ = sys.argv[1]
f__ = f_.split(".")
x_ = []
y_ = []
leg = []
for c in range(-1, 31):
	if c == -1:
		f_temp = f_
	else:
		f_temp = f__[0] + ",SERVICE_CATEGORY_ID=" + str(c) + ".out"
	if not os.path.isfile(f_temp):
		continue
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

fig = plt.figure()
grid()
ax = fig.add_subplot(111)    # The big subplot
y_max = -1
for i in range(len(x_[0])):
	print x_[0][i],":",
	for j in range(len(x_)):
		if x_[0][i] in x_[j]:
			print y_[j][x_[j].index(x_[0][i])],"(",leg[j],")",
		else:
			print 0, "(", leg[j],")",
	print ""

	
for i in range(len(x_)):
	ax.plot(x_[i], y_[i])
	print min(x_[i]), max(x_[i])
	y_max = max(y_max, max(y_[i]))
ax.set_ylim([-1, y_max*1.5])
#ax.set_xlim([-0.5, 6.5])
ax.legend(leg, fontsize=20, ncol=2)
ax.set_xlabel("Timestamp", fontsize=20)
ax.set_ylabel(f_.split("~")[1], fontsize=20)
ax.set_title(f_.split("~")[2].split(".")[0], fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(x_tick)#, rotation='30')
plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("%s_combine.png"%(f_), bbox_inches='tight')
