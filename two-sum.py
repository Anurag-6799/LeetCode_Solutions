#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if target-nums[i] in mp.keys():
                return [mp[target-nums[i]],i]
            else:
                mp[nums[i]] = i
        return [0,0]
# @lc code=end

