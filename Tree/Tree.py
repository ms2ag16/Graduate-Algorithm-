class TreeNode(object):
  def __init__(self, x=-1, left=None, right=None):
    self.val=x
    self.left=left
    self.right=right

class Tree(object):
  def __init__(self):
    self.root=TreeNode()
    self.myQueue=[]
  
  def add(self, val):
    node=TreeNode(val)
    if self.root.val==-1:
      self.root=node
      self.myQueue.append(self.root)
    
      
