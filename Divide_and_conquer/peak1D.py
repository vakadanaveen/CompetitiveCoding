class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:return 0
        if nums[0]>nums[1]:
            return 0
        elif nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            m=(l+r)//2
            if m!=0 and m!=n-1 and nums[m]>nums[m-1] and nums[m]>nums[m+1]:
                return m
            elif nums[m]<nums[m-1]:
                r=m-1
            else:
                l=m+1
        return -1
                
        