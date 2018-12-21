class TreeNode(object):
  def __init__(self, x=-1):
    self.val=x
    self.left=None
    self.right=None
  def printTree(self):
    print self.val

class Tree(object):
  def __init__(self):
      self.root=TreeNode()
      self.queue=[]
  def add(self, x):
      node=TreeNode(x)
      if self.root is None:
          self.root=node
          self.queue.append(self.root)
      else:
          treeNode=self.queue[0]
          if treeNode.left==None:
              treeNode.left=node
              self.queue.append(treeNode.left)
          else:
              treeNode.right=node
              self.queue.append(treeNode.right)
              self.queue.pop(0)
    
  
    

    
