class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        d=0
        for i in range(len(nums)):
            if nums[i] !=val:
                nums[d]=nums[i]
                d+=1
        return d