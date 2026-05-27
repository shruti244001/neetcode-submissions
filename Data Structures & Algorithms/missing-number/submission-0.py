class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # SumOfNNum=0
        # SumOfnums=0
        # for i in range(len(nums)+1):
        #     SumOfNNum+=i
        # for i in range(len(nums)):
        #     SumOfnums+=nums[i]
        # return SumOfNNum-SumOfnums
        n=len(nums)
        SumOfNNum=0
        SumOfnums=0
        for i in range(n+1):
            SumOfNNum^=i
        for i in nums:
            SumOfnums^=i
        return (SumOfNNum^SumOfnums)
        

