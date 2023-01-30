

def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i - 1
        while j >= 0 and key < input_array[j]:
            input_array[j + 1] = input_array[j]
            j -= 1
        input_array[j + 1] = key
    return input_array