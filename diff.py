#How number of free slots and bikes change each time
#Run: python diff.py log_file
import sys

pre_bike = [0 for i in range(322)]
pre_free = [0 for i in range(322)]
count = 0
out = open(sys.argv[1] + ".diff", "w")
with open(sys.argv[1]) as f:
	for line in f:
		values = line.split("\t")
		if len(values) != 10:
			continue
		idx = int(values[1])
		free = int(values[4])
		bike = int(values[5])
		if count > 0:
			diff_free = free - pre_free[idx]
			diff_bike = bike - pre_bike[idx]
			out.write(values[1] + "\t" + values[2] + "\t" + str(diff_free) + "\t" + str(diff_bike) + "\n")
		pre_free[idx] = free
		pre_bike[idx] = bike
		count += 1
out.close()
