"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true

"""

""" two pass idea """

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = decrease = True
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                decrease = False
            if A[i] > A[i + 1]:
                increase = False
        return increase or decrease


    def isMonotonic2(self, A):
        return all(A[i]>=A[i+1] for i in range(len(A)-1)) or all(A[i]<A[i+1] for i in range(len(A)-1))