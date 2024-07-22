import sys

infi = sys.argv[1]

with open(infi,"r") as f:
	lines = [line.strip() for line in f.readlines()]

with open(infi,"w") as f:
	for line in lines:
		if line == "":
			f.write("EMPTY\n")
		else:
			f.write(line+"\n")
