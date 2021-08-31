def countingSort(a, exp):
    n = len(a)
    res,acum =[0]*(n),[0] * (10)
    for i in range(0, n):
        index = (a[i] / exp)
        acum[int(index % 10)] += 1
    for i in range(1, 10):
        acum[i] += acum[i - 1]
    i = n - 1
    while i >= 0:
        index = (a[i] / exp)
        res[acum[int(index % 10)] - 1] = a[i]
        acum[int(index % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(a)):
        a[i] = res[i]
 
def radixSort(a):
    max1,exp=max(a),1
    while max1/exp > 0:
        countingSort(a, exp)
        exp*=10
 
#Test Cases
#arreglo = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
arreglo = [45,89,234,27,9,45,21,87,15,2458,152,18,8,0]
radixSort(arreglo)
print("Resultado:")
for i in range(len(arreglo)):
    print(arreglo[i])