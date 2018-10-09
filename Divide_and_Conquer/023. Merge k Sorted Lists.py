"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""





class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return None
        res = []
        pairs = length / 2
        if length % 2 == 1:
            res.append(lists[-1])
        for i in range(pairs):
            res.append(self.merge2Lists(lists[i * 2], lists[i * 2 + 1]))

        if len(res) == 1:
            return res[0]
        else:
            return self.mergeKLists(res)

    def merge2Lists(self, l1, l2):
        head=point=ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                point.next=l1
                l1=l1.next
            else:
                point.next=l2
                l2=l2.next
            point=point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
