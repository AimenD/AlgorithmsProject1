import time
def quick_select(arr, left, right, k, counters):
    """
    Quick Select algorithm implementation with operation counting.
    """
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right, counters)
    
    # The pivot is in its final sorted position
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k, counters)
    else:
        return quick_select(arr, pivot_index + 1, right, k, counters)
    

def partition(arr, left, right, counters):
    """
    Partitions the array around the pivot element chosen to be the first element of the array.
    Includes counting of comparisons and swaps.
    """
    pivot = arr[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        counters['comparisons'] += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            counters['swaps'] += 1
    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    counters['swaps'] += 1
    return i - 1

def select(arr):
    """
    Finds the ⌈n/2⌉'th element using the Quick Select algorithm with operation counting.
    """
    n = len(arr)
    k = (n - 1) // 2 + (n % 2)
    counters = {'comparisons': 0, 'swaps': 0}
    median = quick_select(arr, 0, n - 1, k, counters)
    return median, counters
# Example call (commented out):
# find_ceiling_median_quick_select([12, 11, 13, 5, 6])

with open("r1000.txt", "r") as file:
    data = file.readlines()
    for line in data:
        input = line.split()
    input = [int(i) for i in input]
    t_start = time.time()

    median, counters  = select(input)
    t_end = time.time() 


    print("\n\nFor ",file.name )
    print("------------------------")
    print("Median is: ", median)
    print("------------------------")
    print(f"Execution Time in (s): {t_end-t_start}")
    print("------------------------")
    print("Number of operations:", counters['swaps'] + counters['comparisons'])
    print("------------------------\n")



