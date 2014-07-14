total = 0.0

for count in range(1,10000001,4):
    total=total+(1./float(count))-(1./float(count+2))
    print "> %.80f" % (total*4)
print "%.80f" % (total*4)
