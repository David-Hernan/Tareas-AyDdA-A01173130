def maxHeapify(a, n, i):
    largest = i 
    left,right = 2 * i + 1, 2 * i + 2 
    if left < n and a[largest] < a[left]:
        largest = left
    if right < n and a[largest] < a[right]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]  
        maxHeapify(a, n, largest)

def buildMaxHeap(a):
    for i in range(len(a)//2 - 1, -1, -1):
        maxHeapify(a, len(a), i)

def heapSort(a):
    buildMaxHeap(a)
    for i in range(len(a)-1, 0, -1):
        a[i], a[0] = a[0], a[i] 
        maxHeapify(a, i, 0)

#Test Cases
#arreglo = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
arreglo = [45,89,234,27,9,45,21,87,15,2458,152,18,8,0]
heapSort(arreglo)
print("Resultado:")
for i in range(len(arreglo)):
    print(arreglo[i]),