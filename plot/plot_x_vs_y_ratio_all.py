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

def get_neighbor_x_y(nid):
	global neis, x_all, y_all
	if nid in neis:
		nn = neis[nid]
		print "\tgetting neighbors:", nn
	else:
		print "\tmissing neighbor:", nid
		return [], [], []
	data = open(sys.argv[2]).readlines()
	x_ = []
	y_ = []
	z_ = []
	for n in nn:
		if not n in x_all:
			print "\t\tmissing neighbor %s for %s"%(n, nid)
			continue
		x_.append(x_all[n])
		y_.append(y_all[n])
		z_.append(n)
	return x_, y_, z_

neis = {}
data = open("neighbors.x2").readlines()
for l in data:
	s = l.split("|")
	s[1] = s[1].upper()
	s[2] = s[2].upper()
	if s[1] in neis:
		neis[s[1]].append(s[2][:-1])
	else:
		neis[s[1]] = [s[2][:-1]]

#print neis

x_all = {}
y_all = {}
data = open(sys.argv[2]).readlines()
l = 0
print "Getting \"all\" file..."
while l < len(data)/5:
	domain_id = data[l*5][:-1]
	print "", domain_id
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
	for t_ in t:
		y.append(int(t_))
	x, y = add_zero(x, y)
	x_all[domain_id] = x
	y_all[domain_id] = y
	l += 1

print ""

leg = []
aa = []
b = []
aa_ = []
b_ = []
data = open(sys.argv[1]).readlines()
l = 0
while l < len(data)/5:
	domain_id = data[l*5][:-1]
	print domain_id
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
	for t_ in t:
		y.append(int(t_))
	x, y = add_zero(x, y)
	x_nei, y_nei, id_nei = get_neighbor_x_y(domain_id)
	for i in range(len(x)):
		t = x[i]
		for ii in range(len(x_nei)):
			if not t in x_nei[ii]:
				continue
			i2 = x_nei[ii].index(t)
			aa.append(y[i])
			b.append(y_nei[ii][i2])
			aa_.append(domain_id)
			b_.append(id_nei[ii])
	l += 1

fig = plt.figure()
gs = gridspec.GridSpec(2,1,height_ratios=[2,1])
ax = plt.subplot(gs[0])    # The big subplot
ax2 = plt.subplot(gs[1])    # The big subplot



print aa
print b

max_aa = {} 
max_b = {}

for x in aa_:
	if not x in max_aa:
		max_aa[x] = -1
for x in b_:
	if not x in max_b:
		max_b[x] = -1
for i in range(len(aa)):
	if aa[i]>max_aa[aa_[i]]:
		max_aa[aa_[i]] = aa[i]
for i in range(len(b)):
	if b[i]>max_b[b_[i]]:
		max_b[b_[i]] = b[i]


y = {}
for i in range(101):
	y[i] = []
for i in range(len(aa)):
	if aa[i] == 0:
		x = 0
	else:
		x = int(aa[i]*100.0/max_aa[aa_[i]])
	if b[i] == 0:
		y[x].append(0)
	else:
		y[x].append(b[i]*100.0/max_b[b_[i]])
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
ax.set_xlim([-1, 101])
#ax.legend(leg, fontsize=20, ncol=2)
ax.set_xticks([0,20,40,60,80,100])
ax.set_xticklabels(["", "", "", "", "", ""])
#ax.set_xlabel("Streaming Traffic of ", fontsize=20)
ax.set_ylabel("Overall Utilization", fontsize=20)
#ax.set_title(enb1 + " vs. " + enbdd2, fontsize=18)

t = 0
for i in range(101):
	t += len(y[i])
y_p = []
for i in range(101):
	y_p.append(len(y[i])*1.0/t)
ax2.plot(range(101), y_p, "x")
ax2.set_xlim([-1,101])
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
fig.savefig("errorbar_ratio_all.png", bbox_inches='tight')
