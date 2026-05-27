class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
            helper(path,i+1)

        helper([],0)
        return res
