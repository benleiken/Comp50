#Word_Count.py
print "Please enter the filename of the text file you'd like to get a word count for"
fname = raw_input()
f = open(fname,'r')
landmarks =dict()
y = 1
while (y):
	line = f.readline()
	if not line:
		break
	line.lower()
	list = line.split()
	for i in range (len(list)):
		if list[i] in landmarks:
			landmarks[list[i]] += 1
		else:
			landmarks[list[i]] = 1
for key in sorted(landmarks):
	print key + "    " + str(landmarks[key])
count = 0
for key in sorted(landmarks):
	count += landmarks[key]
print "There are " + str(count) + " words in " + fname
f.close()