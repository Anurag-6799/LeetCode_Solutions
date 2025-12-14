class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for num in nums:
            if mp.get(num):
                mp[num]+=1
            else: mp[num]=1
        for i in mp.values():
            if i>1:
                return True
        return False