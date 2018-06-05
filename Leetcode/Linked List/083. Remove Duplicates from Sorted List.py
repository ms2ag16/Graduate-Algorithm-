# Definition for singly-linked list. 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Example 1: 
# Input: 1->1->2
# Output: 1->2
    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def my_print(self):
        print (self.val)
        if self.next:
            print(self.next.val)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        while curr:
            while curr.next and curr.val==curr.next.val:
                curr.next=curr.next.next
            curr=curr.next
        return head
        
if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3
    r = Solution().deleteDuplicates(n1)
    r.my_print()
