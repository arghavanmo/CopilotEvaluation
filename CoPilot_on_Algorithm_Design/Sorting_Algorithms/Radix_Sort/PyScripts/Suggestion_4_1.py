

#!/usr/bin/env python3
# Path: algorithm_design/s/random.py
# Compare this snippet from algorithm_design/s/insertion_sort.py:
# # create a function to sort an array of size n in ascending order:
# # 1: Iterate from arr[0] to arr[n] over the array.
# # 2: Compare the current element (key) to its predecessor.
# # 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
# # source https://www.geeksforgeeks.org/insertion-sort/?ref=lbp - accessed on 30/03/2022
# import random
# 
# 
def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == ""__main__"":
    test = [random.randint(0, 100) for _ in range(10)]
    print(test)
    print(insertion_sort(test))
# 
#Given an array of integers, where each element has d digits, where the first digit is the lowest order digit, and the last digit is the highest order digit, sort the array in ascending order by first comparing the lowest order digits and then higher order digits. the sorting should be done in linear time
#!/usr/bin/env python3
# Path: algorithm_design/s/random.py
# Compare this snippet from algorithm_design/s/insertion_sort.py:
# # create a function to sort an array of size n in ascending order:
# # 1: Iterate from arr[0] to arr[n] over the array.
# # 2: Compare the current element (key) to its predecessor.
# #"