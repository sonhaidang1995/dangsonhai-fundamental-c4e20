adult = 1
teenage = 0
children = 0
print("Month 0: 1 pair(s) of rabbit")
for i in range (1,5):
    adult = adult + teenage
    teenage = children
    children = adult
    n = adult + teenage + children
    print("Month {}: {} pair(s) of rabbit".format(i,n))