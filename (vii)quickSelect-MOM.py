import time

def quick_select_median_of_medians(arr, left, right, k, counters):

    if left == right:
        return arr[left]

    pivot_index = median_of_medians_partition(arr, left, right, counters)
    
    if pivot_index == -1:  # Error handling if pivot not found
        return None

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select_median_of_medians(arr, left, pivot_index - 1, k, counters)
    else:
        return quick_select_median_of_medians(arr, pivot_index + 1, right, k, counters)

def median_of_medians_partition(arr, left, right, counters):

    if right - left + 1 <= 5:
        # Find the median directly for small subarrays
        median_index = select_median(arr, left, right)
        return partition(arr, left, right, median_index, counters)
    
    subarray_medians = []
    for i in range(left, right + 1, 5):
        sub_right = min(i + 4, right)
        median_index = select_median(arr, i, sub_right)
        subarray_medians.append(arr[median_index])

    mid_median = quick_select_median_of_medians(subarray_medians, 0, len(subarray_medians) - 1, len(subarray_medians) // 2, counters)
    median_index = arr.index(mid_median)

    return partition(arr, left, right, median_index, counters)

def partition(arr, left, right, pivot_index, counters):

    pivot = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    counters['swaps'] += 1
    store_index = left
    for i in range(left, right):
        counters['comparisons'] += 1
        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            counters['swaps'] += 1
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]
    counters['swaps'] += 1
    return store_index

def select_median(arr, left, right):

    sublist = arr[left:right + 1]
    sublist.sort()
    return left + len(sublist) // 2

def select(arr):

    counters = {'comparisons': 0, 'swaps': 0}
    n = len(arr)
    k = (n - 1) // 2 + (n % 2)
    median = quick_select_median_of_medians(arr, 0, n - 1, k, counters)
    return median, counters
# Example testing

with open("r1000.txt", "r") as file:
    data = file.readlines()
    for line in data:
        input = line.split()
    input = [int(i) for i in input]
    t_start = time.time()

    median,counters = select(input)
    t_end = time.time() 

    print("\n\nFor ",file.name )
    print("------------------------")
    print("Median is: ", median)
    print("------------------------")
    print(f"Execution Time in (s): {t_end-t_start}")
    print("------------------------")
    print("Number of operations:", counters['swaps'] + counters['comparisons'])
    print("------------------------\n")



