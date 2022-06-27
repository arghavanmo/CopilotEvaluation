

def sort(arr):
    sorted_list = []
    unsorted_list = arr
    while len(unsorted_list) > 0:
        smallest = unsorted_list[0]
        for i in range(1, len(unsorted_list)):
            if unsorted_list[i] < smallest:
                smallest = unsorted_list[i]
        sorted_list.append(smallest)
        unsorted_list.remove(smallest)
    return sorted_list

