#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1

        left_max =0
        right_max =0
        ans = 0

        while left<right:
            if height[left]<=height[right]:
                if left_max>height[left]:
                    ans+=(left_max-height[left])
                else:
                    left_max = height[left]
                left+=1
            else:
                if right_max>height[right]:
                    ans+=(right_max-height[right])
                else:
                    right_max = height[right]
                right-=1
        return ans
        
# @lc code=end

