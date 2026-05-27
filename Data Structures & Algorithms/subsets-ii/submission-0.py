class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def helper(path,i):
            if i==len(nums):
                res.append(path.copy())
                return
            
            #include
            path.append(nums[i])
            helper(path,i+1)
            path.pop()

            #exclude
            idx=i+1
            while idx<len(nums) and nums[idx]==nums[idx-1]:
                idx+=1
            helper(path,idx)

        helper([],0)
        return res
