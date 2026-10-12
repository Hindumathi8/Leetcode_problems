class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=0
        for i in digits:
            s=i+s*10
        l=s+1
        r=[int(d) for d in str(l)]
        return r