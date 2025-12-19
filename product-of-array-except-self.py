#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1=1
        ans = []
        for num in nums:
            if len(ans)<=len(nums):
                ans.append(prod1)
                prod1*=num
        prod2=1
        for i in range(-1, -1 * len(nums)-1, -1):
            ans[i]*=ans[i]
            prod2*=nums[i]
        return ans

# @lc code=end

