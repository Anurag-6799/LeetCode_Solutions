#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        while left<right and left<len(height) and right>=0:
            ln = min(height[left], height[right])
            width = abs(right-left)
            ans = max(ans,ln*width)
            l = max(height[left], height[right])
            if l!=height[left]:
                left+=1
            else:
                right-=1
        return ans
# @lc code=end

