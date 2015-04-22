import matplotlib
matplotlib.use('Agg')
import glob, os, sys, re, math, operator
import matplotlib.pyplot as plt
import plot_lib
from pylab import *
from mpltools import color

top = 15

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
data = open(f_).readlines()
l = 0

x_ = []
y_ = []
leg = []
while l < len(data)/5:
	domain_id = int(data[l*5])
	t = data[l*5+2].split(",")[:-1]
	x = []
	for t_ in t:
		x.append(int(t_))
	trans(x)	

	if len(x) == 0:
		l += 1
		continue

	t = data[l*5+4].split(",")[:-1]
	y = []
	tt = plot_lib.get_legend("DOMAIN_ID", domain_id)[:10]
	if tt == "-1":
		tt = "Unknown:" + str(domain_id)
	leg.append(tt)
	for t_ in t:
		y.append(int(t_))
	
	print tt
	x, y = add_zero(x, y)
	print x
	print y
	x_.append(x)
	y_.append(y)

	x_tick = range(0, max(x)+24, 24)
	l += 1

x__ = []
y__ = []
leg__ = []
sum_ = {}
for t in y_:
	sum_[sum(t)] = y_.index(t)
sorted_sum = sorted(sum_.items(), key=operator.itemgetter(0), reverse=True)

for t in sorted_sum[:top]:
	print t
	x__.append(x_[t[1]])
	y__.append(y_[t[1]])
	leg__.append(leg[t[1]])

x_ = x__
y_ = y__
leg = leg__


fig = plt.figure()
color.cycle_cmap(len(x_), cmap='gist_rainbow')
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
	y_max = max(y_max, max(y_[i]))
ax.set_ylim([-1, y_max*1.5])
#ax.set_xlim([-0.5, 6.5])
ax.legend(leg, fontsize=10, ncol=3)
ax.set_xlabel("Timestamp", fontsize=20)
ax.set_ylabel(f_.split("~")[1], fontsize=20)
ax.set_title(f_.split("~")[2].split(".")[0], fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(x_tick)#, rotation='30')
plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("separate_%s.png"%(f_), bbox_inches='tight')
