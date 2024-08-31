#
#
# def counting_sort(arr):
#     max_val = max(arr)
#     min_val = min(arr)
#
#     range_of_elements = max_val - min_val + 1
#
#     count_arr = [0] * range_of_elements
#
#     output_arr = [0] * len(arr)
#
#     for num in arr:
#         count_arr[num - min_val] += 1
#
#     for i in range(1, len(count_arr)):
#         count_arr[i] += count_arr[i - 1]
#
#     for num in reversed(arr):
#         output_arr[count_arr[num - min_val] - 1] = num
#         count_arr[num - min_val] -= 1
#
#     return output_arr
#
# def count_sort_median(arr):
#     sorted_arr = counting_sort(arr)
#     # Bse case: if the array has 0 or 1 element, the array is already sorted
#     n = len(sorted_arr)
#     if n == 1:
#         return sorted_arr[0]
#
#     if n == 0:
#         return 0
#     # when the length of the sorted array is not even
#     if n % 2 != 0:
#         return sorted_arr[n//2]
#     else:
#         return (sorted_arr[n//2] + sorted_arr[n//2 + 1]) / 2
#
#
#
# def activityNotifications(expenditure, d):
#     # determine the total numbers of notification a client received over a period of n days
#     # when n is len(expenditure)
#
#     total_number_of_notification = 0
#     n = len(expenditure) #
#
#     left_pointer = 0
#     right_pointer = d
#
#     if n <= d:
#         return total_number_of_notification
#
#     while left_pointer < right_pointer <= n - 1:
#         print(" i got here", left_pointer, right_pointer)
#         median_expenditure = count_sort_median(expenditure[left_pointer:right_pointer])
#         print("runing expediture_array", expenditure[left_pointer:right_pointer])
#         print("median_expenditure", median_expenditure)
#         if expenditure[right_pointer] >= 2 * median_expenditure:
#             total_number_of_notification += 1
#         left_pointer += 1
#         right_pointer += 1
#     return total_number_of_notification
#
#
# expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# d = 5
# print("activityNotifications")
# print(activityNotifications(expenditure, d))

# print("2 activeNotifications")
# expenditure = [10, 20, 30, 40, 50]
# d = 3
# print("activityNotifications")
# print(activityNotifications(expenditure, d))

def quick_sort_with_median(arr):
    print('arr', arr)
    n = len(arr)

    if n == 0:
        raise ValueError("Cannot calculate median for an empty array")  # Error for empty array

    if n == 1:
        return arr, arr[0]  # Array is sorted, median is the only element

    # Step 1: Choose the pivot element
    pivot = arr[n // 2]
    print('pivot', pivot)

    # Step 2: Partition the array into three sublists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Step 3: Recursively apply quick sort to the left and right sub-arrays
    sorted_left, _ = quick_sort_with_median(left) if left else ([], None)
    sorted_right, _ = quick_sort_with_median(right) if right else ([], None)

    # Concatenate the results to form the sorted array
    sorted_arr = sorted_left + middle + sorted_right

    # Calculate the median for the entire sorted array
    n_sorted = len(sorted_arr)
    if n_sorted % 2 != 0:
        median = sorted_arr[n_sorted // 2]  # Median for an odd-length array
    else:
        median = (sorted_arr[n_sorted // 2 - 1] + sorted_arr[n_sorted // 2]) / 2  # Median for an even-length array

    return sorted_arr, median

to_find_median = [2, 3, 4, 2, 3, 6, 8, 4, 5]
print(quick_sort_with_median(to_find_median), "my median")


# def quick_sort_median(arr):
#     sorted_arr = quick_sort(arr)
#     # Bse case: if the array has 0 or 1 element, the array is already sorted
#     n = len(sorted_arr)
#     if n == 1:
#         return sorted_arr[0]
#
#     if n == 0:
#         return 0
#     # when the length of the sorted array is not even
#     if n % 2 != 0:
#         return sorted_arr[n//2]
#     else:
#         return (sorted_arr[n//2] + sorted_arr[n//2 + 1]) / 2



# def activityNotifications(expenditure, d):
#     # determine the total numbers of notification a client received over a period of n days
#     # when n is len(expenditure)
#
#     total_number_of_notification = 0
#     n = len(expenditure) #
#
#     left_pointer = 0
#     right_pointer = d
#
#     if n <= d:
#         return total_number_of_notification
#
#     while left_pointer < right_pointer <= n - 1:
#         print(" i got here", left_pointer, right_pointer)
#         median_expenditure = quick_sort_median(expenditure[left_pointer:right_pointer])
#         print("runing expediture_array", expenditure[left_pointer:right_pointer])
#         print("median_expenditure", median_expenditure)
#         if expenditure[right_pointer] >= 2 * median_expenditure:
#             total_number_of_notification += 1
#         left_pointer += 1
#         right_pointer += 1
#     return total_number_of_notification


import heapq


def add_number(num, left_heap, right_heap):
    if not left_heap or num <= -left_heap[0]:
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    # Balance the heaps
    if len(left_heap) > len(right_heap) + 1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif len(right_heap) > len(left_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))


def remove_number(num, left_heap, right_heap):
    if num <= -left_heap[0]:
        left_heap.remove(-num)
        heapq.heapify(left_heap)
    else:
        right_heap.remove(num)
        heapq.heapify(right_heap)

    # Balance the heaps
    if len(left_heap) > len(right_heap) + 1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif len(right_heap) > len(left_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))


def get_median(left_heap, right_heap):
    if len(left_heap) > len(right_heap):
        return -left_heap[0]
    return (-left_heap[0] + right_heap[0]) / 2


def activityNotifications(expenditure, d):
    if len(expenditure) <= d:
        return 0

    left_heap = []  # Max-heap (inverted values for min-heap behavior)
    right_heap = []  # Min-heap

    total_notifications = 0

    # Initialize heaps with the first d elements
    for i in range(d):
        add_number(expenditure[i], left_heap, right_heap)

    for i in range(d, len(expenditure)):
        median = get_median(left_heap, right_heap)
        if expenditure[i] >= 2 * median:
            total_notifications += 1

        # Remove the element going out of the window
        remove_number(expenditure[i - d], left_heap, right_heap)
        # Add the new element in the window
        add_number(expenditure[i], left_heap, right_heap)

    return total_notifications


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
print("activityNotifications")
print(activityNotifications(expenditure, d))

print("2 activeNotifications")
expenditure = [10, 20, 30, 40, 50]
d = 3
print("activityNotifications")
print(activityNotifications(expenditure, d))


def find_median(count_arr, d):
    """
    Finds the median from the frequency array (count_arr) for the window of size d.
    """
    total = 0
    half_d = d // 2
    for i in range(len(count_arr)):
        total += count_arr[i]
        if total >= half_d + (d % 2):  # For odd-sized window, median is the half_d + 1-th smallest
            if d % 2 == 0:
                # Even-sized window: find the average of the two middle elements
                second_median = i
                total -= count_arr[i]
                if total >= half_d:
                    return (i + second_median) / 2.0
                return i
            return i

def activityNotifications(expenditure, d):
    """
    Determines the number of notifications a client receives over a period of n days.
    """
    if len(expenditure) <= d:
        return 0

    max_val = max(expenditure)
    min_val = min(expenditure)
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements

    total_notifications = 0

    # Initialize the counting sort array for the first window
    for i in range(d):
        count_arr[expenditure[i] - min_val] += 1

    for i in range(d, len(expenditure)):
        # Find the median for the current window
        median = find_median(count_arr, d)

        # Check if the notification condition is met
        if expenditure[i] >= 2 * median:
            total_notifications += 1

        # Update the counting sort array for the sliding window
        count_arr[expenditure[i] - min_val] += 1
        count_arr[expenditure[i - d] - min_val] -= 1

    return total_notifications