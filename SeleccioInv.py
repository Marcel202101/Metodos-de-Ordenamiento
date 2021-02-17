v = [47, 3, 21, 32, 56, 92]
print(v)
print("Ordenar:")
for i in range(len(v)):
    minimo = i
    for j in range(i+1, len(v)):
        if(v[j] > v[minimo]):
            minimo = j
    temp = v[i]
    v[i] = v[minimo]
    v[minimo] = temp
    print(v)
    
