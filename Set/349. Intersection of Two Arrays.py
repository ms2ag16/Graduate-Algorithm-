"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1=set([])
        set2=set([])
        res=[]
        for num in nums1:
            if num not in set1:
                set1.add(num)
        for num in nums2:
            if num not in set2:
                set2.add(num)
        for num in set1:
            if num in set2:
                res.append(num)
        return res
