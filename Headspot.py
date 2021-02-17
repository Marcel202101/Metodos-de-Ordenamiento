def heapsort(lista,tam):
    for k in range(tam-1,-1,-1):
        for i in range(0,k):
            item=lista[i]
            j=(i+1)/2
            while (j>=0 and lista[int(j)]<item):
                lista[int(i)]=lista[int(j)]
                i=j
                j=j/2
            lista[int(i)]=item
        temp=lista[0];
    lista[0]=lista[k];
    lista[k]=temp;
 
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print(lista[i])
 
"""def leeLista():
    lista=[]
    cn=int(input("Cantidad de numeros a ingresar: "))
 
    for i in range(0,cn):
        lista.append(int(input("Ingrese numero %d : " % i)))
    return lista
"""

#A=leeLista()
A = [7,6,5,8,6,9,1,2]
heapsort(A,len(A))
imprimeLista(A,len(A))