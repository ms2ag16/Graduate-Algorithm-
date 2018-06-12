""" 
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myprint(self):
        print(self.val)
        if self.next:
            self.next.myprint()


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if (n-m)<=0:
            return head
        dummy=ListNode(0)
        dummy.next=head
        point=dummy

        for _ in range(m-1):
            node=point.next

        prev=point.next
        cur=prev.next

        for _ in range(n-m):
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        point.next.next=cur
        point.next=prev
        return dummy.next




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
    result = Solution().reverseBetween(l1, 2,4)
    result.myprint()
