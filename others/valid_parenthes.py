class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0 or stack.pop(-1) != '(': return False
            elif s[i] == '{':
                stack.append(s[i])
            elif s[i] == '}':
                if len(stack) == 0 or  stack.pop(-1) != '{': return False
            elif s[i] == '[' :
                stack.append(s[i])
            elif s[i] == ']':
                if len(stack) == 0 or  stack.pop(-1) != '[': return False
        return len(stack) == 0

s = Solution()
print("Success") if s.isValid("()") else print("Fail")
print("Success") if s.isValid("()[]{}") else print("Fail")
print("Success") if s.isValid("(]") == False else print("Fail")
print("Success") if s.isValid("(]") == False else print("Fail")
print("Success") if s.isValid("([)]") == False else print("Fail")
print("Success") if s.isValid("{[]}") else print("Fail")
print("Success") if s.isValid("]") == False  else print("Fail")
