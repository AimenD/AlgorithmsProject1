import time
# pass index of array to swap
def swap(array, a, b,counter):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    counter['swaps'] += 1  # Counting each swap




def partition(array, first, last,counter):
    # setting pivot as first element
    pivot = array[first]
    # indexing first and last element
    i = first
    j = last
    # until i and j elements cross each other swap function set pivot
    while i < j:
        # increment i element until finds an element greater than pivot
        while i <= last and array[i] <= pivot:
            i += 1
            counter['comparisons'] += 1  # Counting comparisons

        # decrement j element until finds an element less than pivot
        while j >= first and array[j] > pivot:
            j -= 1
            counter['comparisons'] += 1  # Counting comparisons

        if i < j:
            swap(array, i, j,counter)

    swap(array, first, j,counter)
    return j


def sort(array, first, last,counter):
    if first < last:
        # p is pivot index after partitioning
        p = partition(array, first, last,counter)
        # recursively sort, left and right of pivot
        sort(array, first, p - 1,counter)
        sort(array, p + 1, last,counter)
        return array,counter

counter = {'comparisons': 0, 'swaps': 0}


# Read data from file and sort the array
with open("r1000.txt", "r") as file:
    data = file.readlines()
    for line in data:
        input = line.split()

    input = [int(i) for i in input]
    t_start = time.time()
    sorted_array, opcount = sort(input,0, len(input)-1,counter)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(sorted_array)):
        print(sorted_array[i], end=" ")
    median_index = -(-len(sorted_array) // 2)  # This is an alternative way of doing ceil(n/2)
    median = sorted_array[median_index - 1]  # Adjust for zero indexing

    print("\n\nFor ",file.name )
    print("------------------------")
    print("Median is: ", median)
    print("------------------------")
    print(f"Execution Time in (s): {t_end-t_start}")
    print("------------------------")
    print("Number of operations:", counter['swaps'] + counter['comparisons'])
    print("------------------------\n")





