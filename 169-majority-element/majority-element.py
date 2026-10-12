class Solution:
    def majorityElement(self, nums: list[int]) -> int:
       counts={}
       cutoff=(len(nums)/2)

       for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                 counts[i]=1
            
            if counts[i] > cutoff:
                return i