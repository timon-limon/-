def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sortedArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binarySearch(sortedArray, target)
if result != -1:
    print("Элемент найден на позиции:", result)
else:
    print("Элемент не найден")
