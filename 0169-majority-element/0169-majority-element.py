class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l={}
        for i in nums:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        return max(l, key=l.get)