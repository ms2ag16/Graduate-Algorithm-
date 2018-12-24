// in-order traversal
void inOrderTraversal(TreeNode node){
    if (node!=null){
        inOrderTraversal(node.left);
        visit(node);
        inOrderTraversal(node.right);
    }
}

// pre-order traversal
void preOrderTraversal(TreeNode node){
    if (node!=null){
        visit(node);
        preOrderTraversal(node.left);
        preOrderTraversal(node.right);
    }
}

// post-order traversal
void postOrderTraversal(TreeNode node){
    if (node!=null){
        postOrderTraversal(node.left);
        postOrderTraversal(node.right);
        visit(node);
    }
}
