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
	for i in range(a, b+1, 15):
		xx.append(i)
		if i in x:
			yy.append(y[x.index(i)])
		else:
			yy.append(0)
	return xx, yy

def trans_hour(a):
	for i in range(len(a)):
		a[i]=a[i]*1.0/60

f_ = sys.argv[1]
data = open(f_).readlines()
l = 0

x_ = []
y_ = []
leg = []
while l < len(data)/5:
	domain_id = data[l*5]
	t = data[l*5+2].split(",")[:-1]
	x = []
	for t_ in t:
		x.append(int(t_))
	#trans(x)	

	if len(x) == 0:
		l += 1
		continue

	t = data[l*5+4].split(",")[:-1]
	y = []
	#tt = plot_lib.get_legend("DOMAIN_ID", domain_id)[:10]
	#if tt == "-1":
	#	tt = "Unknown:" + str(domain_id)
	leg.append(domain_id)
	for t_ in t:
		y.append(float(t_))
	
	x, y = add_zero(x, y)
	print x
	print y
	x_.append(x)
	y_.append(y)

	x_tick = range(0, int(max(x)+1), 60)
	l += 1

print x_
print y_
y_max = -1
x_max = -1
for i in range(len(x_)):
	x_max = max(x_max, max(x_[i]))
	y_max = max(y_max, max(y_[i]))
y_t = []
x_t = []
for i in range(0, x_max+1, 15):
	tt = 0
	print i
	for t in range(len(x_)):
		if i in x_[t]:
			tt += y_[t][x_[t].index(i)]
			print y_[t][x_[t].index(i)],
	print ""
	print tt
	y_t.append(tt)
	x_t.append(i)
t_y = sum(y_t)

x__ = []
y__ = []
leg__ = []
#x__.append(x_t)
#y__.append(y_t)
leg__.append("Total (100%)")

sum_ = {}
for t in y_:
	sum_[sum(t)] = y_.index(t)
sorted_sum = sorted(sum_.items(), key=operator.itemgetter(0), reverse=True)

for t in sorted_sum[:top]:
	x__.append(x_[t[1]])
	y__.append(y_[t[1]])
	leg__.append(leg[t[1]]+" (" + str(sum(y_[t[1]])*10000/t_y/100.0) + "%)")

x_ = x__
y_ = y__
leg = leg__
	
fig = plt.figure()
color.cycle_cmap(len(x_), cmap='gist_rainbow')
grid()
ax = fig.add_subplot(111)    # The big subplot

trans_hour(x_t)
ax.plot(x_t, y_t, "k")
for i in range(len(x_)):
	trans_hour(x_[i])
	ax.plot(x_[i], y_[i])
'''
for i in range(len(x_[0])):
	print x_[0][i],":",
	for j in range(len(x_)):
		if x_[0][i] in x_[j]:
			print y_[j][x_[j].index(x_[0][i])],"(",leg[j],")",
		else:
			print 0, "(", leg[j],")",
	print ""
'''

print x_t
print y_t
	

ax.set_ylim([-1, max(y_t)*1.5])
ax.set_xlim([0, x_max*1.0/60])
x_tick = range(0, (x_max+1)/60, 24)
ax.legend(leg, fontsize=10, ncol=3)
ax.set_xlabel("Timestamp", fontsize=20)
print f_
fie = f_.split("~")[0]
la = ""
if fie == "4":
	la = "Downlink PRB"
else:
	la = "Uplink PRB"
ax.set_ylabel(la, fontsize=20)
ax.set_title(f_.split(".")[0], fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(x_tick)#, rotation='30')
plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("prb_%s.png"%(f_), bbox_inches='tight')
