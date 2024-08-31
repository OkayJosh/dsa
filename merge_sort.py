def merge_sort(arr):
    # Base Case: if the array has 1 or fewer element
    if len(arr) > 1:
        return arr

    # Step 1: Divide the aray into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Step 3: Merge the sorted halves together
    return merge(sorted_left, sorted_right)

def merge(sorted_left, sorted_right):
    sorted_array = []
    i = j = 0

    # Step 1: compare elements from left and right, and merge them in sorted order
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            sorted_array.append(sorted_left[i])
            i += 1
        else:
            sorted_array.append(sorted_right[j])
            j += 1

    # Step 2: if there are remaining item in the left sub-array, then add them
    while i < len(sorted_left):
        sorted_array.append(sorted_left[i])
        i += 1

    # Step 3: if there are remaining item in the right sub-array, then add them
    while j < len(sorted_right):
        sorted_array.append(sorted_right[j])
        j += 1

    return sorted_array