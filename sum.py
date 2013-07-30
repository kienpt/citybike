#How number of free slots and bikes change each time
#Run: python diff.py log_file
import sys
from math import *

out = open(sys.argv[1] + ".sum", "w")
bikes = 0
free = 0
with open(sys.argv[1]) as f:
	for line in f:
		values = line.strip("\n").split("\t")
		bikes = bikes + fabs(int(values[2]))
		free = free + fabs(int(values[3]))
out.write(str(bikes) + "\t" + str(free) + "\n")
out.close()
