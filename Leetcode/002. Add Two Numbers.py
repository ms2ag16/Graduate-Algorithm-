""" 
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. 
"""

# The point is linked-list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
          
    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        dummy=ListNode(0)
        p=dummy

        while l1 or l2 or carry:
            sum,carry=carry,0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            if sum>9:
                carry=1
                sum-=10
            p.next=ListNode(sum)
            p=p.next

        if carry>0:
            dummy.next=ListNode(carry)

        return dummy.next

if __name__=="__main__":
    l1=ListNode(9)
    l1.next=ListNode(9)
    print (Solution().addTwoNumbers(l1,ListNode(1)).myPrint())
