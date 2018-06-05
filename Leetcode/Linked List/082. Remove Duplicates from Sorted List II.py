""" 
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

    def my_print(self):
        print(self.val)
        if self.next:
            print(self.next.val)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy =ListNode(0)
        dummy.next=head
        cur=dummy
        is_repeat=False
        while cur.next:
          while cur.next.next and cur.next.val=cur.next.next.val:
            cur.next=cur.next.next
            is_repeat=True
          if is_repeat:
            cur.next=cur.next.next
            is_repeat=False
          else:
            cur=cur.next
         return dummy.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3=ListNode(2)
    n4 = ListNode(2)

    n1.next = n2
    n2.next = n3
    n3.next=n4
    r = Solution().deleteDuplicates(n1)
    r.my_print()
