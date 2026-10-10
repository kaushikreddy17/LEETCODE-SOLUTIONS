class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        un=1

        for i in range(len(nums)):
            if nums[un-1] != nums[i]:
                nums[un]=nums[i]
                un+=1
        return un