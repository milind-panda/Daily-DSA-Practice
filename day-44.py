class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    seen = set()
        result = []

        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)

        return ''.join(result)
	            
