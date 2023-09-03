class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        res = "" 
        
        for i in range(len(s)):
            # odd cases like abcba, expand from the same place 
            p1 = self.findPalindrome(s, i, i)
            # even cases like abba, expands from two consecutive indices 
            p2 = self.findPalindrome(s, i, i+1)
            
            res = max(p1, p2, res, key = len)
        
        return res 
        
    def findPalindrome(self, s, l, r):
        ## expand a palindrome with left and right index l and r
        ## l and r are initialized to be the center index 
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # the indices in the non-inclusive interval (l,r) belongs to the palindrome
        # since python indices includes the left but not the right
        # we need pass l+1 and r
        return s[l+1:r]
        
result = Solution().longestPalindrome("abcbad")
pass 