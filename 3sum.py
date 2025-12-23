3#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
def moveleft(nums, left):
    existingvalue = nums[left]
    while left<len(nums) and nums[left]==existingvalue:
        left+=1
    return left
def moveright(nums, right):
    existingvalue = nums[right]
    while right>=0 and nums[right]==existingvalue:
        right-=1
    return right
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            right = len(nums)-1
            left  = None
            if i+1<len(nums):
                left = i+1
            if not left:
                break
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                if sum==0:
                    ans.append([nums[i],nums[left], nums[right]])
                    left = moveleft(nums, left)
                    right = moveright(nums, right)
                elif sum<0:
                    left = moveleft(nums, left)
                else:
                    right = moveright(nums, right)
        return ans
# @lc code=end

