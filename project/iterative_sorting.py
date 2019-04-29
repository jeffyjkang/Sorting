#import this
#import antigravity
# Complete the selection_sort() function below in class with your instructor
animal = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
          'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


def selection_sort(arr):
    # loop through each index in the arr, stop at length of array, non-inclusive
    for i in range(len(arr)):
        # initialize the current index we are working on with the i-th index, starts at 0
        cur_index = i
        # initialize the smallest index to the current index to compare
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # another loop, start at current index, end at last index in array
        for j in range(cur_index, len(arr)):
            # if condition, value at array at index j is smaller than value of current smallest index
            if arr[j] < arr[smallest_index]:
                # reassign the smallest index to index j
                smallest_index = j
        # TO-DO: swap
        # swap that with the current element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    # return sorted array
    return arr


# print(animal)
selection_sort(animal)
print(animal)

# TO-DO: implement the Insertion Sort function below


# separate first element from rest of array, own array called sorted
# begin with 1, copy item at that index into temp variable, iterate to left until you find correct index of sorted array
# insert at that position of the array, shift rest of the items to the right

# animal = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
#           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

def insertion_sort(arr):
    # step through each index, i in range 1 through length of arr non inclusive, start at 1 because if starting at 0, nothing to compare to the left of index
    for i in range(1, len(arr)):
        # temp is value at each index to compare to left of or the index, which is at first arr at index of 1 then iterates to 2, 3, 4...
        temp = arr[i]
        # value directly left is initialized to j, at the beginning of comparison
        j = i-1
        # keep comparing further and further left until the beginning of arr or index of 0, not past 0 because there is no index less than 0
        while j >= 0:
            # if temp which is index, is less than the element directly left, shift temp one to the left
            if temp < arr[j]:
                # shift whatever element at j to the right if the value of index of i or temp is less than the value directly left of it
                arr[j+1] = arr[j]
                # then shift temp or element at index to the left, if value of index or temp is less than the value directly left of it
                arr[j] = temp
                # decrement j which is initially the value directly left of temp, down one value, to preform loop over again, j will now be two to the left of i then 3 and 4... if applicable
                j -= 1
                # if the temp is not less than value you are comparing it to break from the loop, no need to shift anymore values left and right
            else:
                break
    # once we are done sorting within the range we can return the sorted arr
    return arr


insertion_sort(animal)
print(animal)

# STRETCH: implement the Bubble Sort function below

# robot, two short arms can only sort directly next to each other


def bubble_sort(arr):
    # walk through the array, comparing each element to its right neightbor
    # repeat this until you make it through an entire pass without any swaps
    # initialize is_sorted variable(bool) to false,
    is_sorted = False
    # loop through until while condition is_sorted is true
    while not is_sorted:
        # check that exits loop if next loop if condition is not met
        is_sorted = True
        # walk through the array, until index of last index -1, this is needed because
        # we are comparing the current index with the next index
        for i in range(len(arr) - 1):
            # comparing each element to its right neighbor
            # if it's smaller than the neighbor,
            if arr[i] > arr[i + 1]:
                # swap the elements
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # if condition is met, reassign the is_sorted to false
                is_sorted = False
    # return array
    return arr


# STRETCH: implement the Count Sort function below

numbers = [1, 4, 9, 2, 1, 5, 9, 3, 5, 7, 1, 6, 8, 8, 3, 3, 2]


def count_sort(arr, maximum=-1):
    # create a count list of zeros, of length maximum + 1, this will count for,
    # all available options including zero
    # reassign maximum to the max value of all elements in list
    maximum = max(arr)
    # assign count list to a list of zeros with length maximum +1
    count_list = [0]*(maximum+1)
    # for each element in the arr
    for a in arr:
        # increment the count_list value at specified index by 1
        count_list[a] += 1
    # to keep track of sorted array index, initialize i to 0
    i = 0
    # loop through the count_list, starting from 0th index
    for c in range(len(count_list)):
        # while loop, value of count_list at index c
        while count_list[c] > 0:
            # reassign value of arr at index i to index c
            arr[i] = c
            # increment i by 1
            i += 1
            # decrement the value of count_list at index c by 1
            count_list[c] -= 1
    # return sorted arr
    return arr


count_sort(numbers)
print(numbers)
