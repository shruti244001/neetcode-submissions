class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        # # return len(nums) != len(set(nums))

        # nums.sort()
        # for index in range(1, len(nums)):
        #     if nums[index] == nums[index - 1]:
        #         return True
        # return False