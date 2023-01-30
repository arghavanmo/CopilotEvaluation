

# # merge sort is a divide and conquer algorithm. it works by recursively splitting the array into smaller pieces until each piece is a single element. then, it combines the two sorted pieces.
# # the time complexity is O(n log n)
# # the space complexity is O(n)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] > right[0]:
        return [right[0]] + merge(left, right[1:])
    else:
        return [left[0]] + merge(left[1:], right)


# ! These were generate by CoPilot ALONGSIDE the function.
# def test_bubble_sort():
#     print(""Testing bubble sort"")
#     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
#     print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


# def test_quick_sort():
#     print(""Testing quick sort"")
#     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
#     print(quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


# def test_merge_sort():
#     print(""Testing merge sort"")
#     print(""Should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"")
#     print(mer"