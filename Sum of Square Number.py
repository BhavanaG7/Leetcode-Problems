'''
Leetcode Link:https://leetcode.com/problems/sum-of-square-numbers/
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
'''

class Solution:
    def judgeSquareSum(self, c):
        import math

        cc=int(math.sqrt(c))
        l=0
        r=cc

        while l<=r:
            mid=l**2+r**2

            if mid== c:
                return True
            elif mid<c:
                l+=1
            else:
                r-=1
        return False
