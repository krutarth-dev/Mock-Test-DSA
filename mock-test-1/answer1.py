def moveZeroes(nums):
    n = len(nums)
    j = 0

    # Iterate through the array
    for i in range(n):
        # If the current element is non-zero
        if nums[i] != 0:
            # Swap the current element with the element at position j
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums
nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))

nums2 = [0]
print(moveZeroes(nums2))
