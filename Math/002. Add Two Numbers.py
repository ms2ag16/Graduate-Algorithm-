"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
""" 

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def addNum(n1, n2):
            if not n1 and not n2:
                return 0
            if not n2:
                return n1.val
            if not n1:
                return n2.val
            return n1.val + n2.val

        cur=ListNode(0)
        res=cur
        while l1 or l2:
            cur.val+=addNum(l1, l2)
            if cur.val>=10:
                cur.val-=10
                cur.next=ListNode(1)
            else:
                if l1 and l1.next or l2 and l2.next:
                    cur.next=ListNode(0)
            cur=cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return res
        
        

                
            
            
            
            
            
          
