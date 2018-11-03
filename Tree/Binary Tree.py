from Tree import Tree


class BinaryTree(Tree):
    """ An abstract base class representing a binary structure. """

    # --- additional abstract methods---------
    def left(self, p):
        """ return a Position representing p's left child,
        return None if p does not have a left child. """
        raise NotImplementedError(' must be implemented by subclass ')

    def right(self, p):
        """ return a Position representing p's right child,
        return None if p does not have a right child. """
        raise NotImplementedError(' must be implemented by subclass ')

    # ---------- concrete method implemented in this class --------
    def sibling(self, p):
        """ return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ generate an iteration of Position representing p's children. """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
