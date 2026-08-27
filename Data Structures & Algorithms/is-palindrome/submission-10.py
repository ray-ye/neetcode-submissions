class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""

        for c in s:
            if c.isalpha() or c.isdigit():
                s_new += c

        s_new = s_new.lower()

        for i in range(len(s_new)):
            if s_new[i] != s_new[-(i+1)]:
                return False
        
        return True