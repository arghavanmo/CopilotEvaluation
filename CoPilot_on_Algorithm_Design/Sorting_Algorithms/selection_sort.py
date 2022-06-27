# create a function that accepts an array as input. the function will create two lists, one named sorted and the other unsorted. at the begning, the unsorted list will be the same as the input array.
# ! Below comment was generated by CoPilot ALONGSIDE the function. It also generated an algorithm for selection sort!
# # # the function will iterate through the unsorted list. at each iteration, it will find the smallest element in the unsorted list and append it to the sorted list.
# # # the time complexity is O(n^2)
# # # the space complexity is O(1)


def selection_sort(arr):
    sorted_list = []
    unsorted_list = arr
    while unsorted_list:
        smallest = unsorted_list[0]
        for element in unsorted_list:
            if element < smallest:
                smallest = element
        sorted_list.append(smallest)
        unsorted_list.remove(smallest)
    return sorted_list


# # ! These were generate by CoPilot ALONGSIDE the function.
# # def test_selection_sort():
# #     print("Testing selection sort")
# #     print("Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# #     print(selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
#
#
# # def test_merge_sort():
# #     print("Testing merge sort")
# #     print("Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# #     print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
#
#
# # def test_quick_sort():
# #     print("Testing quick sort")
# #     print("Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# #     print(quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
#
#
# # def test_bubble_sort():
if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 56, 6]
    selection_sort(test)
