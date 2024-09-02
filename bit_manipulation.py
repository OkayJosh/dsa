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