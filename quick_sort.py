def quick_sort(arr):
    """
    Perform Quick Sort on the given array.

    Quick Sort is a divide-and-conquer algorithm that selects a pivot element from the array
    and partitions the other elements into two sub-arrays, according to whether they are less than
    or greater than the pivot. The sub-arrays are then sorted recursively.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new list that is sorted in ascending order.
    """
    # Bse case: if the array has 0 or 1 element, the array is already sorted
    if len(arr) <= 1:
        return arr

    # step 1: choose the pivot element
    pivot = arr[len(arr) // 2]

    # step 2: partition the array into 3 list
    left = [ x for x in arr if x < pivot ]
    middle = [ x for x in arr if x == pivot ]
    right = [ x for x in arr if x > pivot ]

    # step 3: recursively apply quick sort to the left and right sub-arrays
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + middle + sorted_right
