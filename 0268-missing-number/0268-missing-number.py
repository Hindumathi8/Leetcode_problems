class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==m:
                l=m+1
            else:
                r=m-1
        return l


                    