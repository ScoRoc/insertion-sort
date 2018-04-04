
def insertion_sort(arr):
    for i in range(1, len(arr)):

        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    return arr


my_array = [4, 92, 1, 39, 19, 93, 49, 10, 99, 103, 13, 102, 32, 345, 145, 4590, 111, 56, 167, 2101]

print(insertion_sort(my_array))
    
