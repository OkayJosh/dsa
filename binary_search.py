def binary_search(arr, target):
    """
    Perform Binary Search on a sorted array to find the index of the target element.

    Binary Search is a divide-and-conquer algorithm that repeatedly divides the search space in half,
    comparing the target element to the middle element of the current sub-array, and narrowing down
    the search to the left or right half based on the comparison.

    Parameters:
    arr (list): The sorted list of elements in which to search.
    target: The element to search for.

    Returns:
    int: The index of the target element in the array if found, otherwise -1.
    """
    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        # Step 1: find the middle element
        mid_index = (left_index + right_index) // 2

        # Step 2: compare the target element with the middle element
        if arr[mid_index] == target:
            return mid_index
            # Target is found at the middle index
        elif arr[mid_index] < target:
            left_index = mid_index + 1
            # Target is on the right, discard the left element
        else:
            right_index = mid_index - 1
            # Target is on the left, we discard the right elements

    return -1