"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""

class RandomListNode(object):
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        visited=dict()
        m=n=head
        while m:
            visited[m]=RandomListNode(m.label)
            m=m.next
        while n:
            visited[n].next=visited.get(n.next)
            visited[n].random=visited.get(n.random)
            n=n.next
        return visited.get(head)
    
          
        
