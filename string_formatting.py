


num = input()
bnum = len(str("{0:b}".format(num)))
# print bnum


for i in xrange(1,num+1):
	print ("{0:d}".format(i)).rjust(bnum)+'\t'+("{0:o}".format(i)).rjust(bnum)+'\t'+("{0:X}".format(i)).rjust(bnum)+'\t'+("{0:b}".format(i)).rjust(bnum)




