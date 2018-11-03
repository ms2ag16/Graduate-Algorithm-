from Priority_Queues import  PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
    """ a min-oriented priority queue implemented with a sorted list"""

    def __init__(self):
        """ create a new empty Priority Queue. """
        self._data=PositionalList()

    def __len__(self):
        """ return the number of items in the priority queue. """
        return len(self._data)

    def add(self, key, value):
        """ add a key-value pair """
        newest = self._Item(key, value)  # make a new item instance
        walk = self._data.last()  # walk backward looking for a smaller key
        while walk is not None and newest < walk.element():
            walk=self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)      # new kwy is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        """ return but do not remove (k,v) tuple with minimum key """
        if self.is_empty():
            raise Empty('Priority queue is empty. ')
        p= self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """ remove and return (k,v) tuple with minimum key. """
        if self.is_empty():
            raise Empty (' Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
    