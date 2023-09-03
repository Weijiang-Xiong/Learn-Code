# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

from lcutils import * 

class Solution:
    """ consider a sliding window with a start and end idx (both initialized to 0)
    go through the string and put the end pointer to the position being inspected 
    use a dict to store the last seen position of characters
    maintain the start pointer in the following way to ensure there is no repeat 
    between start and end: 
        1. if the character being inspected (idx) has been seen before, and the 
        last seen position is not to the left of start, move the start to the immediate 
        right position of the last seen
        2. otherwise just update the max length by comparing current value and the 
        number of elements from start to idx 
        
    
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = maxlen = 0 
        seen  = dict() 
        for idx, char in enumerate(s): 
            if char in seen and seen.get(char, 0)>=start: 
                start = seen[char] + 1 
            else:
                maxlen = max(maxlen, idx - start + 1)
                
            seen[char] = idx
            
        return maxlen

        
        