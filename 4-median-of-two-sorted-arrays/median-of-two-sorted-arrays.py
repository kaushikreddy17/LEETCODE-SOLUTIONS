
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        l=len(arr)
        if l%2==0:
            return (arr[l//2-1]+arr[l//2])/2
        else:
            return arr[l//2]