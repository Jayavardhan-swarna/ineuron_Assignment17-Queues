def maxSubarraySumCircular(nums):
    # Kadane's algorithm with modification for circular property
    curr_max = nums[0]
    curr_min = nums[0]
    max_sum = nums[0]
    min_sum = nums[0]
    total_sum = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_sum = max(max_sum, curr_max)
        curr_min = min(nums[i], curr_min + nums[i])
        min_sum = min(min_sum, curr_min)
        total_sum += nums[i]

    if max_sum > 0:
        return max(max_sum, total_sum - min_sum)
    else:
        return max_sum


print(maxSubarraySumCircular([1, -2, 3, -2]))  # Output: 3
print(maxSubarraySumCircular([5, -3, 5]))      # Output: 10
print(maxSubarraySumCircular([-3, -2, -3]))    # Output: -2
