m = [3, 13, 8, 25, 45, 23, 98, 58]
n = len(m)
for i in range(n):
    pos = i
    while( pos>0 and m[pos]<m[pos-1]):
        temp = m[pos-1]
        m[pos-1] = m[pos]
        m[pos] = temp
        pos -= 1
    print(m)

