"""
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myprint(self):
        print(self.val)
        if self.next:
            self.next.myprint()


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        count=0
        if not head:
            return head
        while p.next:
            p=p.next
            count+=1
        shift=count-k%count
        p.next=head
        for i in range(0,shift):
            p=p.next
        head=p.next
        p.next=None
        return head

 if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    result = Solution().rotateRight(l1, 2)
    result.myprint()          
            
       
