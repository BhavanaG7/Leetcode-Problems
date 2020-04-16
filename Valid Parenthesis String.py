'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
'''

class Solution:
    def checkValidString(self, s):
        if len(s)==0 or s=="*":
            return True

        if len(s)==1:
            return False

        left=0
        for i in s:
            if i==")":
                left-=1
            else:
                left+=1

            if left<0:
                return False
        if left==0:
            return True

        right=0
        for i in reversed(s):
            if i=="(":
                right-=1
            else:
                right+=1

            if right<0:
                return False
        return True

s=input()
obj=Solution()
print(obj.checkValidString(s))