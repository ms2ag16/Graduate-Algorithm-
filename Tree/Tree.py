class Tree:
    """ abstract base class representing a tree structure"""
    # -- nested Position class --
    class Position:
        """ an abstraction representing the location of a single element"""
        def element(self):
            """ return the element stored at this position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """ :return true if other position represents by subclass """
            raise NotImplementedError(" must be implemented by subclass ")

        def __ne__(self, other):
            """ :return true if other does not represent the same location"""
            return not(self==other)

    # --abstract methods that concrete subclass must support ------
    def root(self):
        """ :return position representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self,p):
        """ return position representing p's parent"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self,p):
        """ return the number of children that position p has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self,p):
        """ generate an iteration of Positions representing p's children."""
        raise NotImplementedError(' must be implemented by subclass. ')

    def __len__(self):
        """ return the total number of elements in the tree. """
        raise NotImplementedError(' must be implemented by subclass. ')

    # -- concrete methods implemented in this class ----
    def is_root(self,p):
        """ return True if Position p represents the root of the tree. """
        return self.root()==p

    def is_leaf(self,p):
        """ return True if Position p does not have any children. """
        return self.num_children(p)==0

    def is_empty(self):
        """ return True if the tree is empty """
        return len(self)==0

    def depth(self,p):
        """ return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1+ self.depth(self.parent(p))

    def _height1(self): # works ,O(n^2) worst case
        """ return the height of the tree. """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """ return the height of the subtree rooted at Position p.
            if p==none, return the height of entire tree .
        """
        if p is None:
            p=self.root()
        return self._height2(p) # start _height2 recursion






