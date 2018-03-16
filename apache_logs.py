import collections

logfile = open("log.txt", "r")

clean_log = []

for line in logfile:
	try:
		clean_log.append(line)
	except:
		pass

counter = collections.Counter(clean_log)

#print(counter)

for count in counter.most_common(10):
	print(str(count[1]) + "   " + str(count[0]))

logfile.close()
