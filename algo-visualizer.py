def bubble_sort(arr):
    for i in range(len(
        arr)):
        for j in range(0, len(arr)-i-1
                       ):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
    return arr

# def quick_sort(arr):

# def radix_sort(arr):

def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)
        
    return -1
        

