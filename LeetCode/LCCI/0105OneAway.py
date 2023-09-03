class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """

        if first==second: # both empty or the same 
            return True
        if len(first)*len(second)==0 and len(first)+len(second)==1: # one of them is empty, the other is one char
            return True
        if abs(len(first) - len(second)) > 1: # can not fix 2 chars within 1 edit 
            return False
        if first[0] == second[0]:
            return self.oneEditAway(first[1:], second[1:])
        else: # I need to make an edit 
            if first[1:] == second[0:] or \
                first[0:]==second[1:] or \
                first[1:]==second[1:]:
                return True
            else:
                return False   
            
s = Solution() 
print(s.oneEditAway("islander", "slander"))