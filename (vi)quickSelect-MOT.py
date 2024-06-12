import time

def quick_select_median_of_three(arr, left, right, k, counters):

    if left == right:
        return arr[left]

    pivot_index = median_of_three_partition(arr, left, right, counters)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select_median_of_three(arr, left, pivot_index - 1, k, counters)
    else:
        return quick_select_median_of_three(arr, pivot_index + 1, right, k, counters)

def median_of_three_partition(arr, left, right, counters):

    mid = (left + right) // 2
    # Sort the first, middle, last elements and choose the median as the pivot.
    pivot_candidates = [(arr[left], left), (arr[mid], mid), (arr[right], right)]
    pivot_candidates.sort(key=lambda x: x[0])
    counters['comparisons'] += 2  # Two comparisons in sorting three elements
    median_value, median_index = pivot_candidates[1]

    arr[left], arr[median_index] = arr[median_index], arr[left]
    counters['swaps'] += 1  # Swap the median to the first position
    pivot = arr[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        counters['comparisons'] += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            counters['swaps'] += 1
            i += 1
    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    counters['swaps'] += 1
    return i - 1

def select(arr):

    counters = {'comparisons': 0, 'swaps': 0}
    n = len(arr)
    k = (n - 1) // 2 + (n % 2)
    median = quick_select_median_of_three(arr, 0, n - 1, k, counters)
    return median, counters



with open("r15000.txt", "r") as file:
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





