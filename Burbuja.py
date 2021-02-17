m = [47, 3, 21, 32, 56, 92]
print(m)
n = len(m)-1
for i in range(n):
    for j in range(n):
        if(m[j]>m[j+1]):
            temp = m[j]
            m[j] = m[j+1]
            m[j+1] = temp
    print(m)
    
'''m = [47, 3, 21, 32, 56, 92]
print(m)
n = len(m)-1
for i in range(n):
    for j in range(n):
        if(m[j]<m[j+1]):
            temp = m[j]
            m[j] = m[j+1]
            m[j+1] = temp
    print(m)
'''