from lcutils import * 

class Solution:
    keyMap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return [] 
        if len(digits) == 1:
            return list(self.keyMap[digits])
        
        combs = list(self.keyMap[digits[0]])
        for key in digits[1:]:
            combs = self.add_key(combs, key)
        return combs 

        
    def add_key(self, string_combs, key):
        
        extended_combs = [] 
        chars_to_append = self.keyMap[key]
        for comb in string_combs:
            for char in chars_to_append:
                extended_combs.append(comb+char)
        return extended_combs 
    
    
digits = "23"
combs = Solution().letterCombinations(digits)
print(combs)