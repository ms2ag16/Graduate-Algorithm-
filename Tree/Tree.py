class TreeNode(object):
  def __init__(self, x=-1, left=None, right=None):
    self.val=x
    self.left=left
    self.right=rig

class Tree(object):
  def __init__(self):
    self.root=TreeNode()
    self.myQueue=[]
  
  def add(self, val):
      node=TreeNode(val)
      if self.root.val==-1:
          self.root=node
          self.myQueue.append(self.root)
      else:
          treebide=self.myQueue[0]
            if treenode.left==None:
                treenode.left=None
                self.myQueue.append(treenode.left)
            else:
                treenode.right=node
                self.myQueue.append(treenode.right)
                self.myQueue.pop(0)
  
  def front_recursive(self, root):
        if root ==None:
            return
        
    
      
