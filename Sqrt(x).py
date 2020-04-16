'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

'''

class Solution:
    def mySqrt(self, x):
        l=0
        r=x

        while l<=r:
            mid=(l+r)//2
            mid_sqr=mid*mid

            if mid_sqr<=x:
                l=mid+1
            else:
                r=mid-1
        return l-1