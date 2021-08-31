import random

def BinSea(a,n,k):
    l,r=0,n-1
    while l<=r:
        m = (l+r)//2
        if k == a[m]:
            return m
        elif k < a[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

values = []
for i in range(1,1000):
    values.append(random.randint(1, 1000))
values.sort()
print ( values )
k=25
pos = BinSea(values,len(values),k)
if pos != -1:
    print(str(k)," see encuentra en la posición ", str(pos))
else:
    print(str(k)," no se encuentra en el arreglo")

