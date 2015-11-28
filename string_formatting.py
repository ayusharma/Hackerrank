


num = input()
bnum = len(str("{0:b}".format(num)))+1
print bnum


for i in xrange(1,num+1):
	# print ("{0:d}".format(i)).rjust(bnum)+("{0:o}".format(i)).rjust(bnum)+("{0:x}".format(i)).rjust(bnum)+("{0:b}".format(i)).rjust(bnum)
	print ("{0:d}".format(i)).rjust(bnum)+' '+("{0:o}".format(i)).rjust(bnum)+' '+("{0:x}".format(i)).rjust(bnum)+' '+("{0:b}".format(i)).rjust(bnum)




