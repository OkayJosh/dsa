"""
Bit Manipulation:

Concept
Bit manipulation is a technique that involves working directly with the
binary representation of numbers to perform operations efficiently.
Since computers operate at the binary level, bit manipulation can be
extremely fast and effective for certain types of problems.
This technique is often used in scenarios where arithmetic operations would be
 too slow or cumbersome. Common bitwise operations include
AND, OR, XOR, NOT, left shift, and right shift.


"""
from heap import result


def is_power_of_two(n):
    """
    Implementation to check if an integer number is a power of two.
    In order works can the number be express as a power of two?.
    :param n:
    :return:
    """
    if n < 0:
        return False

    # This expression will be 0 only when n is a power of two.
    return n & (n - 1) == 0


# Test cases
print(is_power_of_two(1))  # True (2^0)
print(is_power_of_two(2))  # True (2^1)
print(is_power_of_two(3))  # False
print(is_power_of_two(16)) # True (2^4)
print(is_power_of_two(16667)) #


def hamming_weight(n):
    """
    Hamming weigh is the number of 1 in the binary representation of integer n.
    :param n:
    :return:
    """
    count = 0
    while n > 0:
        count += n & 1  # Add the least significant bit to the count
        n >>= 1 # Right shift 'n' by 1 bit (i.e., divide by 2)
    return count # Return the total count of '1' bits

count_bits = hamming_weight
print(hamming_weight(1)) # Test cases
print(count_bits(3))   # 2 (binary `11`)
print(count_bits(7))   # 3 (binary `111`)
print(count_bits(15))  # 4 (binary `1111`)


def single_number(nums):
    """
    Given an array where every element appears twice except for one, find that single element.
     XOR operation is perfect for this task because a ^ a = 0 and a ^ 0 = a.
    :param nums:
    :return:
    """

    result = 0
    for num in nums:
        result ^= num
    return result

# Test cases
print(single_number([2, 2, 1]))        # 1
print(single_number([4, 1, 2, 1, 2]))  # 4
print(single_number([1]))              # 1

def missing_number(nums):
    """
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
     find the one number that is missing from the array.
    :param nums:
    :return result:
    """

    n = len(nums)
    # Start with n because we would be XORing from 0 to n
    result = n

    for i in range(n):
        result ^= i ^ nums[i]
        """
        XOR Operation Basics
        First, let's understand a few key properties of the XOR (^) operation:
        
        Same Numbers Cancel Out: If you XOR the same number with itself, you get 0. For example, a ^ a = 0.
        XOR with 0: If you XOR a number with 0, you get the number itself. For example, a ^ 0 = a.
        Order Doesn't Matter: XOR is commutative and associative, which means the order in which you XOR numbers doesn't change the result. For example, a ^ b ^ c is the same as c ^ a ^ b.
        The Problem
        You have an array nums that contains numbers from 0 to n, but one number is missing. You want to find out which number is missing.
        
        The Key Idea
        The trick here is to use the XOR operation to cancel out the numbers that are present in the array. When you XOR all the numbers together, the missing number is the only one that doesn't get canceled out.
        
        Step-by-Step Example: nums = [0, 1, 3]
        Let's walk through the example where nums = [0, 1, 3].
        
        Initialization:
        
        n = len(nums) which is 3 because there are three elements in the array.
        Start with result = n, so result = 3.
        Loop Through the Array:
        
        The loop will run three times, once for each element in the array.
        First Iteration (i = 0):
        result = result ^ i ^ nums[i]
        Substitute values: result = 3 ^ 0 ^ nums[0] = 3 ^ 0 ^ 0 = 3
        After this step, result is still 3.
        Second Iteration (i = 1):
        result = result ^ i ^ nums[i]
        Substitute values: result = 3 ^ 1 ^ nums[1] = 3 ^ 1 ^ 1 = 3
        After this step, result is still 3.
        Third Iteration (i = 2):
        result = result ^ i ^ nums[i]
        Substitute values: result = 3 ^ 2 ^ nums[2] = 3 ^ 2 ^ 3
        Simplify: 3 ^ 3 = 0, so result = 0 ^ 2 = 2
        After this step, result becomes 2.
        Final Result:
        
        After the loop finishes, result holds the value 2, which is the missing number.
        """

    return result


def find_two_non_repeating(nums):
    """
     Given an array where every element appears twice except for two elements
     , find the two non-repeating elements
    :param nums:
    :return [num1, num2]:
    """
    xor_results = 0

    for num in nums:
        xor_results ^= num

    # Find a bit that is set in xor_result
    set_bit = xor_results & -xor_results

    # Partition the numbers based on the set bit
    num1 = num2 = 0

    for num in nums:
        if num & set_bit:
            print(num, set_bit, num & set_bit)
            num1 ^= num
        else:
            print(num, set_bit, num & set_bit)
            # 0010 & 0001
            num2 ^= num

    return [num1, num2]

# Test cases
print("Finding Two Non repeating Numbers")
print(find_two_non_repeating([1, 1, 2, 2, 3, 4]))  # [3, 4] or [4, 3]
print(find_two_non_repeating([5, 7, 5, 8]))  # [7, 8]


def swap_without_temp(a: int, b: int) -> tuple[int, int]:
    """
    Swap the values of two variables without using a temporary variable.
    :param a:
    :param b:
    :return:
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


# Test cases
print(swap_without_temp.__name__)
print(swap_without_temp(5, 10))  # (10, 5)
print(swap_without_temp(7, 14))  # (14, 7)


def find_missing_positive_integer(nums: list[int]) -> int:
    """
    Given an unsorted integer array, find the smallest missing positive integer.
    :param nums:
    :return int:
    """
    n = len(nums)

    # Place each number in its correct position
    for num in range(n):
        while 1 <= nums[num] <= n and nums[nums[num] - 1] != nums[num]:
            nums[nums[num] - 1], nums[num] = nums[num], nums[nums[num] - 1]

    # Find the first index where the number is not correct
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

# Test cases
print(find_missing_positive_integer.__name__)
print(find_missing_positive_integer([3, 4, -1, 1]))  # 2
print(find_missing_positive_integer([1, 2, 0]))  # 3


def are_anagrams(num1, num2):
    """
    Check if two numbers are anagrams of each other in their binary representation.
    :param num1:
    :param num2:
    :return:
    """
    print(hamming_weight(num1), hamming_weight(num2))
    return hamming_weight(num1) == hamming_weight(num2)

# Test cases
print(are_anagrams.__name__)
print(are_anagrams(12, 6))  # True (binary 1100 and 0110)
print(are_anagrams(7, 11))  # False
