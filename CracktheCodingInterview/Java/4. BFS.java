void search(Node root){
    Queue queue = new Queue();
    root,marked = true;
    queue.enqueue(root);
    
    while (!queue.isEmpty()){
        Node r = queue.dequeue();
        visit(r);
        foreach (Node n in r.adjacent){
            if (n.marked ==false){
                n.marked = true;
                queue.enqueue(n);
            }
        }
    }
}
