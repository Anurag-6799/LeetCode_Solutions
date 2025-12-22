#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while True and left<len(s):
            if (ord(s[left])>=65 and ord(s[left])<=90) or (ord(s[left])>=97 and ord(s[left])<=122) or (ord(s[left])>=48 and ord(s[left])<=57):
                break
            left+=1
        while True and right>=0:
            if (ord(s[right])>=65 and ord(s[right])<=90) or (ord(s[right])>=97 and ord(s[right])<=122) or (ord(s[right])>=48 and ord(s[right])<=57):
                break
            right-=1
        while left<right:
            if s[left].lower()==s[right].lower():
                left+=1
                right-=1
                while True and left<len(s):
                    if (ord(s[left])>=65 and ord(s[left])<=90) or (ord(s[left])>=97 and ord(s[left])<=122) or (ord(s[left])>=48 and ord(s[left])<=57):
                        break
                    left+=1
                while True and right>=0:
                    if (ord(s[right])>=65 and ord(s[right])<=90) or (ord(s[right])>=97 and ord(s[right])<=122) or (ord(s[right])>=48 and ord(s[right])<=57):
                        break
                    right-=1
            else:
                return False
        return True

# can clean the code by putting the repeated code in a function and calling it for verification of ascii value
# @lc code=end

