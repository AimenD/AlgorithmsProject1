import time



def sort(arr):
    count = 0

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        sort(left_half)  # Sorting the first half
        sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            count += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            count += 1


        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            count += 1


    return arr,count





# Read data from file and sort the array
with open("r15000.txt", "r") as file:
    data = file.readlines()
    for line in data:
        input = line.split()

    input = [int(i) for i in input]
    t_start = time.time()
    sorted_array, opcount = sort(input)
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
    print(f"Number of operations: {opcount}")
    print("------------------------\n")



