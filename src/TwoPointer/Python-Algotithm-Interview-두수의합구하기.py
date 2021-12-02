def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    left, right = 0, len(nums)-1
    while not left == right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return left, right
