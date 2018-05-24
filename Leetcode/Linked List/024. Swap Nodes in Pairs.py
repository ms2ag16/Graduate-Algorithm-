""" 
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
比较常见的链表操作。下面看一下典型情况，如要交换链表中A->B->C->D中的B和C需要做如下操作：
将A指向C
将B指向D
将C指向B
在头节点之前加一个假节点就可以使所有的交换都符合上面的情况。
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=point=ListNode(0)
        dummy.next=head
        while point.next and point.next.next:
      
            tmp=point.next.next      
            point.next.next=tmp.next     
            tmp.next=point.next     
            point.next=tmp
            point=point.next.next
     return dummy.next

if __name__ == "__main__":
    n5 = ListNode(5)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2 = ListNode(2)
    n1 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result = Solution().swapPairs(n1)
    print (result.myPrint())
