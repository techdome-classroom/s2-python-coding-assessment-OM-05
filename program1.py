class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

# Ensure there's an instance of the class to run if needed
if __name__ == "__main__":
    solution = Solution()




    



  

