class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num=sorted(nums)
        Sum=0
        res=[]
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:continue
            l=i+1
            r=len(nums)-1
            while l<r:
                Sum=num[i]+num[l]+num[r]
                if Sum==0:
                    temp=[num[i],num[l],num[r]]
                    res.append(temp)
                    l+=1
                    r-=1
                    while (l<r and num[l]==num[l-1]):
                        l+=1
                    while (l<r and num[r]==num[r+1]):
                        r-=1
                elif Sum<0:
                    l+=1
                else:
                    r-=1
        return res

