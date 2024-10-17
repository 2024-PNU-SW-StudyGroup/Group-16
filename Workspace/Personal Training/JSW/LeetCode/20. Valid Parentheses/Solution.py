class Solution:
    def isValid(self, s):
        parentheses = {
            '(': ')', 
            '[': ']', 
            '{': '}'
        }
        stack = []
        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                poped_element = stack.pop()
                if c != parentheses[poped_element]:
                    return False
                    
        if len(stack) != 0:
            return False

        return True