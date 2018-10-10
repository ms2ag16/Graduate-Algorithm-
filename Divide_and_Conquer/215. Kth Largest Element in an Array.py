"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""

""" DIVIDE AND CONQUER """
class Solution(object):
       def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        
        
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = self.mergeSort(nums)
        return sorted_nums[len(nums)-k]

    def mergeSort(self, nums):
        if len(nums)==1:
            return nums
        else:
            leftList=self.mergeSort(nums[:len(nums)/2])
            rightList=self.mergeSort(nums[len(nums)/2:])
            return self.merge(leftList,rightList)

    def merge(self, leftList, rightList):
        result, i, j= [], 0,0
        for k in range(len(leftList)+len(rightList)):
            if i<len(leftList) and j <len(rightList):
                if leftList[i]<=rightList[j]:
                    result.append(leftList[i])
                    i+=1
                else:
                    result.append(rightList[j])
                    j+=1
            else:
                result.append(leftList[i] if i<len(leftList) else rightList[j])
                i+=1
                j+=1
        return  result

        
