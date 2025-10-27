def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

test_array = [12, 11, 13, 5, 6]
insertionSort(test_array)
print("Отсортированный массив:", test_array)
