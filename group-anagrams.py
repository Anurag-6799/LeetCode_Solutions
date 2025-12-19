#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            mp[sorted_key].append(s)
        return list(mp.values())
# @lc code=end

