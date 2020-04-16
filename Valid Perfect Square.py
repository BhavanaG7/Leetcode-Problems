'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num):
        l=0
        r=num

        while l<=r:
            mid=(l+r)//2
            mid_sqr=mid*mid

            if mid_sqr==num:
                return True

            elif mid_sqr<num:
                l=mid+1

            else:
                r=mid-1
        return False

