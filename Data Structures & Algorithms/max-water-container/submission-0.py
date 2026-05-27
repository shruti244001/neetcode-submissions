class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        lp=0
        rp=n-1
        max_water=0
        while lp<rp:
            width=rp-lp
            hold_water=min(heights[lp],heights[rp])
            curr_capacity=width*hold_water

            max_water=max(max_water,curr_capacity)
            if heights[lp]<heights[rp]:
                lp+=1
            else:
                rp-=1
        return max_water

        