class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort()
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        if len(l)<3:
            return l[-1]
        else:
            return l[-3]