/* 二叉树结构 */
function Node(data, left, right) {
    this.data = data;
    this.left = left;
    this.right = right;
    this.show = show;
}

function show() {
    return this.data;
}

/* 创建根 */
function BST() {
    this.root = null;
    this.insert = insert;
    this.inOrder = inOrder;
}

/* 节点插入 */
function insert(data) {
    var n = new Node(data, null, null);
    if (root = null) {
        this.root = n;
    } else {
        var current = this.root;
        while (current != null) {
            if (data < current.data) {
                if (current.left) {
                    current = current.left;
                } else {
                    current.left = n;
                    break;
                }
            } else {
                if (current.right) {
                    current = current.left;
                } else {
                    current.right = n;
                    break;
                }
            }
        }
    }
}

/* 中序遍历 */
function inOrder(n) {
    if (n) {
        inOrder(n.left);
        console.log(n.data);
        inOrder(n.right)
    }
}

/* 先序遍历*/
function PreOrder(n){
  if(n){
    console.log(n.data);
    PreOrder(n.left);
    PreOrder(n.right);
  }
}

/* 查找 */
function getMin(){
    var current = this.root;
    while(!(current.left == null )){
        current = current.left;
    }
    return current.data;
}
function getMax(){
     var current = this.root;
    while(!(current.right == null )){
        current = current.right;
    }
    return current.data;
}
function find(data){
    var current = this.root;
    while(current != null){
        if(current.data == data){
            return current;
        }
        else if(data < current.data){
            current = current.left;
        }else{
            current = current.right;
        }
    }
    return null;
}

/* 删除节点 */
function remove(data){
    root = removeNode(this.root, data);
}

function removeNode(node, data){
    if(node == null){
        return null;
    }
    if(data == node.data){
        // 没有子节点的节点
        if(node.left == null && node.right == null){
            return null;
        }
        if(node.left == null){
            return node.right;
        }
        if(node.right == null){
            return node.left;
        }
        // 有两个子节点的节点
        var tempNode = getSmallest(node.right);
        node.data = tempNode.data;
        node.right = removeNode(node.right, tempNode.data);
    }
    else if(data < node.data){
        node.left = removeNode(node.left, data);
    }else if(data > node.data){
        node.right = removeNode(node.right, data);
    }
    return node;
}
