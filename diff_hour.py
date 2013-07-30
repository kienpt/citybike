import sys
from math import *

bikes = [[0 for i in range(24)] for j in range(322)]
free = [[0 for i in range(24)] for j in range(322)]
bikes_all = [0 for i in range(24)]
free_all = [0 for j in range(24)]
infile = sys.argv[1]
out = open(infile + ".hour", "w")
out_allstation = open(infile + ".hour.allstation", "w")
with open(infile) as lines:
	for line in lines:
		values = line.split("\t")
		idx = int(values[0])
		h = int(values[1].split("T")[1].split(":",1)[0])
		bikes[idx][h] += fabs(int(values[2]))
		free[idx][h] += fabs(int(values[3]))
for i in range(322):
	b = str(i)
	f = str(i)
	for j in range(24):
		b = b + "\t" + str(int(bikes[i][j]))
		f = f + "\t" + str(int(free[i][j]))
		bikes_all[j] +=  bikes[i][j]
		free_all[j] += free[i][j]
	out.write(b + "\n")
	out.write(f + "\n")

b = ""
f = ""
for i in range(24):
	b = b + "\t" + str(int(bikes_all[i]))
	f = f + "\t" + str(int(free_all[i]))
out_allstation.write(b.strip("\t") + "\n")
out_allstation.write(f.strip("\t") + "\n")

out.close()
out_allstation.close()
