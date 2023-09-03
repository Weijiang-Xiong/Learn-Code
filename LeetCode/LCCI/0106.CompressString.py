class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        if len(S) <= 1:
            return S
        
        cnt=0 
        coi = S[0] # character of interest
        compressed = ""
        for char in S:
            if char == coi: # extend the current one
                cnt+=1 
            else: 
                # record the current one 
                compressed += coi + str(cnt)
                # start a new one 
                coi = char
                cnt=1
        
        compressed += coi + str(cnt)
        
        return compressed if len(compressed) < len(S) else S
    
print(Solution().compressString("")) 