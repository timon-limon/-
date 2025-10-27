def fibonacciSearch(arr, target):
    n = len(arr)
    fibMm2 = 0
    fibMm1 = 1
    fibM = fibMm2 + fibMm1
    while fibM < n:
        fibMm2 = fibMm1
        fibMm1 = fibM
        fibM = fibMm2 + fibMm1
    offset = -1
    while fibM > 1:
        i = min(offset + fibMm2, n - 1)
        if arr[i] < target:
            fibM = fibMm1
            fibMm1 = fibMm2
            fibMm2 = fibM - fibMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMm2
            fibMm1 = fibMm1 - fibMm2
            fibMm2 = fibM - fibMm1
        else:
            return i
    if fibMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    return -1

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
target = 85
result = fibonacciSearch(arr, target)
if result != -1:
    print("Элемент найден на позиции:", result)
else:
    print("Элемент не найден")
