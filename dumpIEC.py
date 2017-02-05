from .models import *

file1 = open("iec.csv", "r")

tmp = []
for line in file1:
	tmp = line.split('\t')
	IEC.objects.create(iecNo = tmp[0], name = tmp[1])