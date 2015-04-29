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

def get_bytes_per_flow(x1,y1,l1,x2,y2,l2):
	x_ = []
	y_ = []
	l_ = []
	for y in y1:
		l = l1[y1.index(y)]
		if l in l2:
			y__ = y2[l2.index(l)]
			x_.append(y)
			y_.append(y__)
			l_.append(l)

	sor = sorted(x_, reverse=True)

	x__ = []
	y__ = []
	l__ = []
	for t in sor[:10]:
		i = x_.index(t)
		x__.append(x_[i])
		y__.append(y_[i])
		l__.append(l_[i])

		print x_[i]*1.0/y_[i],
	print ""

	return x__, y__, l__

	

ori_name = sys.argv[1]
f_ = ori_name
data = open(f_).readlines()
l = 0

x_b_3 = []
y_b_3 = []
leg_b_3 = []
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
	leg_b_3.append(tt)
	for t_ in t:
		y.append(int(t_))
	
	#print tt
	x, y = add_zero(x, y)
	#print x
	#print y
	x_b_3.append(sum(x))
	y_b_3.append(sum(y))

	x_tick = range(0, max(x)+24, 24)
	l += 1

#print x_b
#print y_b
#print leg_b

tt = ori_name.split("=3")
f_ = tt[0] + "=30" + tt[1]
#print f_
data = open(f_).readlines()
l = 0

x_b_30 = []
y_b_30 = []
leg_b_30 = []
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
	leg_b_30.append(tt)
	for t_ in t:
		y.append(int(t_))
	
	#print tt
	x, y = add_zero(x, y)
	#print x
	#print y
	x_b_30.append(sum(x))
	y_b_30.append(sum(y))

	x_tick = range(0, max(x)+24, 24)
	l += 1

###########

tt = sys.argv[1].split("DL_BYTES")
ori_name = tt[0] + "DL_FLOW_CNT" + tt[1]
f_ = ori_name
data = open(f_).readlines()
l = 0


x_f_3 = []
y_f_3 = []
leg_f_3 = []
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
	leg_f_3.append(tt)
	for t_ in t:
		y.append(int(t_))
	
	#print tt
	x, y = add_zero(x, y)
	#print x
	#print y
	x_f_3.append(sum(x))
	y_f_3.append(sum(y))

	x_tick = range(0, max(x)+24, 24)
	l += 1

#print x_f
#print y_f
#print leg_f

tt = ori_name.split("=3")
f_ = tt[0] + "=30" + tt[1]
#print f_
data = open(f_).readlines()

l = 0

x_f_30 = []
y_f_30 = []
leg_f_30 = []
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
	leg_f_30.append(tt)
	for t_ in t:
		y.append(int(t_))
	
	#print tt
	x, y = add_zero(x, y)
	#print x
	#print y
	x_f_30.append(sum(x))
	y_f_30.append(sum(y))

	x_tick = range(0, max(x)+24, 24)
	l += 1

#print x_b
#print y_b
#print leg_b
print leg_f_3, x_f_3
x_3, y_3, leg_3 = get_bytes_per_flow(x_b_3, y_b_3, leg_b_3, x_f_3, y_f_3, leg_f_3)
print x_3,y_3,leg_3
x_30, y_30, leg_30 = get_bytes_per_flow(x_b_30, y_b_30, leg_b_30, x_f_30, y_f_30, leg_f_30)
print x_30,y_30,leg_30


fig = plt.figure()
color.cycle_cmap(max(len(x_3), len(x_30)), cmap='gist_rainbow')
grid()
ax = fig.add_subplot(111)    # The big subplot

leg = []
for i in range(len(y_3)):
	ax.plot(y_3[i], x_3[i], "x")
	leg.append(leg_3[i])

for i in range(len(y_30)):
	ax.plot(y_30[i], x_30[i], "+")
	leg.append(leg_30[i])
#ax.scatter(y_3, x_3, c="r")
#ax.scatter(y_30, x_30, c="b")
ax.set_xscale('log')
#ax.set_ylim([-1, max(y_t)*1.5])
#ax.set_xlim([-1, x_max])
ax.legend(leg, 4,fontsize=10, ncol=3)
ax.set_ylabel("DL_BYTES", fontsize=20)
ax.set_xlabel("DL_FLOW_CNT", fontsize=20)
#ax.set_title(f_.split("~")[2].split(".")[0], fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
#plt.xticks(x_tick)#, rotation='30')
plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("bytes_per_flow.png", bbox_inches='tight')
