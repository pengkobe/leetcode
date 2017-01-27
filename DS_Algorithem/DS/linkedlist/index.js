function Node(element){
  this.element = element;
}

function LList(){
  this.head = new Node("head");
  this.find = find;
  this.insert = insert;
  this.remove = remove;
  this.display = display;
}

function find(item){
  var currNode = this.head;
  while(currNode.element != item){
    currNode = currNode.next;
  }
  return currNode;
}

function insert(newElement, item){
  var newNode = new Node(newElement);
  var curr = this.find(item);
  newNode.next = curr.next;
  curr.next = newNode;
}

function display(){
  var currNode = this.head;
  while(!(currNode.next == null)){
    print(currNode.next.element);
    currNode = currNode.next;
  }
}

function findPrevious(item){
  var currNode = this.head;
  while(!(currNode.next == null) &&
    (currNode.next.element != item)){
    currNode = currNode.next;
  }
  return currNode;
}

function remove(){
  var prevNode = this.findPrevious(item);
  if(!(prevNode.next == null)){
    prevNode = prevNode.next.next;
  }
}

