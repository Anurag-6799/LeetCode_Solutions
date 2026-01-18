/*
 * @lc app=leetcode id=424 lang=cpp
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
class Solution
{
public:
    int find_max_frequency(vector<int> &mp)
    {
        int mx = 0;
        for (int count : mp)
        {
            mx = max(mx, count);
        }
        return mx;
    }

    int characterReplacement(string s, int k)
    {
        vector<int> mp(26, 0);
        int l = 0;
        int ans = 0;
        for (int r = 0; r < s.size(); r++)
        {
            mp[s[r] - 'A']++;
            int mx_freq = find_max_frequency(mp);
            while ((r - l + 1) - mx_freq > k)
            {
                mp[s[l] - 'A']--;
                l++;
                mx_freq = find_max_frequency(mp);
            }
            ans = max(ans, r - l + 1);
        }

        return ans;
    }
};
// @lc code=end

