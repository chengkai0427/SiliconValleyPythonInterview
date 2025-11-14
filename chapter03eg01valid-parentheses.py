class Solution:
    '''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Note that an empty string is also considered valid.
    '''
    def isValid(self, s: str) -> bool:
        if len(s) % 2 or s=='':
            return False
        stack_dict={'(':')','[':']','{':'}'}
        stack=[]
        for a in s:
            if a in stack_dict:
                stack.append(a)
            else:
                if a not in stack_dict.values():
                    return False
                if stack:
                    if a!=stack_dict[stack.pop()]:
                        return False
                else:
                    return False
        return not stack
# test
for s in ["()[]{}", "()[]{", "()[()]", "([)]{})","))", "({[]}","(((())))"]:
    print(Solution().isValid(s))