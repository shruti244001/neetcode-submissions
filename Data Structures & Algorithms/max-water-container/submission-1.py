class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        lp=0;rp=n-1
        max_water=0

        while lp<rp:
            width=rp-lp
            water_hold=min(heights[lp],heights[rp])

            area=width*water_hold

            max_water=max(max_water,area)

            if heights[lp]<heights[rp]:
                lp+=1
            else:
                rp-=1

        return max_water

