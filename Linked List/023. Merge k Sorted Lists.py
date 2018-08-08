# Definition for singly-linked list.
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
        self.nodes=[]
        head=point=ListNode(0)
        for nodelist in lists:
            while nodelist:
                self.nodes.append(nodelist.val)
                nodelist=nodelist.next
        
        for x in sorted(self.nodes):
            point.next=ListNode(x)
            point=point.next
        
        return head.next
        
        
