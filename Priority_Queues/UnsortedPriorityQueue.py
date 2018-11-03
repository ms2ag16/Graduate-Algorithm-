from Priority_Queues import PriorityQueueBase


def Empty():
    pass

class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        """ Return Position of item with minimum key """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small=self._data.first()
        walk=self._data.after(small)
        while walk is not None:
            if walk.element()< small.element():
                small=walk
            walk=self._data.after(walk)
        return small

    def __init__(self):
        """ create a new empty Priority Queue. """
        self._data=PositionalList()

    def __len__(self):
        """ return the number of items in the priority queue """
        return len(self._data)

    def add(self, key, value):
        """ add a key-value pair """
        self._data.add_last(self._Item(key, value))

    def min(self):
        """ return but do not remove (k,v) tuple with minimun key """
        p=self._find_min()
        item=p.element()
        return (item._key, item._value)

    def remove_min(self):
        """ remove and return (k,v) tuple with minimun key. """
        p=self._find_min()
        item=self._data.delete(p)
        return (item._key, item._value)
