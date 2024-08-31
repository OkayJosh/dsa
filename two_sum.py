def two_sum(nums, target_sum):
    """
    The Algorithm works on sorted arrays
    :param nums:
    :param target_sum:
    :return:
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left +=1
        else:
            right -=1

    return []