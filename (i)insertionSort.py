import time



def insertion_sort(elements):
    count = 0

    for index in range(1, len(elements)):
        current_value = elements[index]
        position = index - 1
        while position >= 0 and elements[position] > current_value:
            elements[position + 1] = elements[position]
            position -= 1
            count += 1  # Counting assignment (swap)

        elements[position + 1] = current_value
        count += 1  # Counting assignment (swap)


    return elements, count




# Read data from file and sort the array
with open("r15000.txt", "r") as file:
    data = file.readlines()
    for line in data:
        input = line.split()

    input = [int(i) for i in input]
    t_start = time.time()
    sorted_array, opcount = insertion_sort(input)
    t_end = time.time()
    print("Sorted array is:")
    for i in range(len(sorted_array)):
        print(sorted_array[i], end=" ")
    print("")

    median=sorted_array[(len(sorted_array) // 2)-1]

    print("\n\nFor ",file.name )
    print("------------------------")
    print("Median is: ", median)
    print("------------------------")
    print(f"Execution Time in (s): {t_end-t_start}")
    print("------------------------")
    print(f"Number of operations: {opcount}")
    print("------------------------\n")
