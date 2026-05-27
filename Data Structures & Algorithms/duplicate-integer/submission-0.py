class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count={}
        # for num in nums:
        
        #     count[num]=count.get(num,0)+1

        # for idx,ele in count.items():
        #     if ele>1:
        #         return True
        # return False
        
        '''optimal code'''
        # seen=set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False 

        '''most optimal'''
        return len(nums)!=len(set(nums))
