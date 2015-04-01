import matplotlib
matplotlib.use('Agg')
import glob, os, sys, re, math, operator
import matplotlib.pyplot as plt

from pylab import *

def trans(a):
	f_day = -1
	f_time = -1
	print a
	for i in range(len(a)):
		t = a[i]
		day = (t % 1000000)/10000
		time = (t % 10000)/100
		if f_day == -1:
			f_day = day
			f_time = time
		a[i] = 24*(day-f_day)+(time-f_time)
	print a


f_ = sys.argv[1]

data = open(f_).readlines()
t = data[1].split(",")[:-1]
x = []
for t_ in t:
	x.append(int(t_))

trans(x)

t = data[3].split(",")[:-1]
y = []
for t_ in t:
	y.append(int(t_))

print x
print y
x_tick = range(0, max(x)+24, 24)

fig = plt.figure()
grid()
ax = fig.add_subplot(111)    # The big subplot
ax.plot(x, y)
#ax.set_ylim([0, 30])
#ax.set_xlim([-0.5, 6.5])
#ax.legend(["NAME", "OPT", "ARI", "PRO", "MOZ", "PJG"], fontsize=22, numpoints=1, ncol=3)
ax.set_xlabel("Timestamp", fontsize=20)
ax.set_ylabel("Metric", fontsize=20)
ax.set_title(f_, fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(x_tick)#, rotation='30')
plt.tight_layout()
#fig.savefig("filesize.eps", bbox_inches='tight')
fig.savefig("%s.png"%(f_), bbox_inches='tight')
