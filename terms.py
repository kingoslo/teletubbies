d = 4
g = [( "g%s(" % str(i) ) for i in range(2**d)]
for k in range(d):
    for j in range(1, 2**(k+1)):
        a = 2**k - abs(2**k-j)
        g[j] = g[j] + "%s/%s+" % (str(a), str(2**k) )
for i in range(len(g)):
    print g[i]