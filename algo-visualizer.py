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

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)


def countingSort(arr, exp1): 
   
    n = len(arr) 
   
    
    output = [0] * (n) 
   
    
    count = [0] * (10) 
   
    
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 

def radixSort(arr):
 
    max1 = max(arr)
 
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10

def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)
        
    return -1
        

