function list(){
  this.listSize = 0;
  this.pos = 0;
  this.dataStore = [];
  this.clear = clear;
  this.find = find;
  this.toString = toString;
  this.insert = insert;
  this.append = appned;
  this.remove = remove;
  this.front = front;
  this.end = end;
  this.prev = prev;
  this.next = next;
  this.length = length;
  this.currPos = currPos;
  this.moveTo = moveTo;
  this.getElement = getElement;
  this.contains = contains;
}

function append(element){
  this.dataStore[this.listSize++] = element;
}


function find(element){
  for (var i = 0; i < this.dataStore.length; i++) {
    if(this.dataStore[i] == element){
      return i;
    }
  }
  return -1;
}

function remove(element){
  var foundAt = this.find(element);
  if(foundAt > -1){
    this.dataStore.splice(foundAt);
    --listSize;
    return true;
  }
}

function insert(element, after){
    var insertPos = this.find(after);
    if(insertPos > -1){
      this.dataStore.splice(insertPos+1, 0, element);
      ++listSize;
      return true;
    }
    return false;
}

function clear(){
  delete this.dataStore;
  this.dataStore.length = 0;
  this.listSize = this.pos = 0;
}

function contains(element){
  for (var i = 0; i < this.dataStore.length; i++) {
    if(this.dataStoreta[i] == element){
      return true;
    }
  return false;
}



