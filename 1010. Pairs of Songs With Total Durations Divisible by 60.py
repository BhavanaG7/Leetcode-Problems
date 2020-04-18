'''
1010. Pairs of Songs With Total Durations Divisible by 60

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
'''

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        import collections
        ans,dict1=0,collections.Counter()
        
        for t in time:
            other_t=(60-(t%60))%60
            ans+=dict1[other_t]
            dict1[t%60]+=1
        return ans

