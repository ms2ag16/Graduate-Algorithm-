# Definition for singly-linked list. 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Example 1: 
# Input: 1->1->2
# Output: 1->2
    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
