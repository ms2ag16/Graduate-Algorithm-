class TreeNode(object):
    def __init__(self, x=-1, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self):
        self.root=TreeNode()
        self.myQueue=[]

    def add(self,val):
        node=TreeNode(val)
        if self.root.val==-1:
            self.root=node
            self.myQueue.append(self.root)
        else:
            treenode=self.myQueue[0]
            if treenode.left==None:
                treenode.left=node
                self.myQueue.append(treenode.left)
            else:
                treenode.right=node
                self.myQueue.append(treenode.right)
                self.myQueue.pop(0)

    def front_recursive(self, root):
        if root==None:
            return
        print root.val
        self.front_recursive(root.left)
        self.front_recursive(root.right)

    def middle_recursive(self, root):
        if root==None:
            return
        self.middle_recursive(root.left)
        print root.val
        self.middle_recursive(root.right)

    def back_recursive(self,root):
        if root==None:
            return
        self.back_recursive(root.left)
        self.back_recursive(root.right)
        print root.val

    def front_stack(self, root):
        if root==None:
            return
        myStack=[]
        while root or myStack:
            while root:
                print root.val
                myStack.append(root)
                root=root.left
            root=myStack.pop()
            root=root.right

    def middle_stack(self, root):
        if root==None:
            return
        myStack=[]
        while root or myStack:
            while root:
                myStack.append(root)
                root=root.left
            root=myStack.pop()
            print root.val
            root=root.right

    def back_stack(self, root):
        if root==None:
            return
        stack2=[]
        stack1=[root]
        while stack1:
            root=stack1.pop()
            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
            stack2.append(root)
        while stack2:
            print stack2.pop().val


    def level_queue(self, root):
        if root==None:
            return
        myQueue=[root]
        while myQueue:
            root=myQueue.pop()
            print root.val
            if root.left:
                myQueue.append(root.left)
            if root.right:
                myQueue.append(root.right)



if __name__ == '__main__':
    nodes = range(3)
    tree = Tree()
    for val in nodes:
        tree.add(val)

    print 'level :'
    tree.level_queue(tree.root)



