class Solution:
    def isBalanced(self, s):
        
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            # Opening bracket
            if ch in "({[":
                stack.append(ch)

            # Closing bracket
            else:
                # No opening bracket available
                if len(stack) == 0:
                    return False

                # Top bracket should match
                if stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        # Stack should be empty
        return len(stack) == 0
