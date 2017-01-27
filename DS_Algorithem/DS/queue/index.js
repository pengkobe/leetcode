function Queue(){
  this.dataStore = [];
  this.enqueue = enqueue;
  this.dequeue = dequeue;
  this.front = front;
  this.back = back;
  this.toString = toString;
  this.empty = empty;
}

function enqueue(element){
  this.dataStore.push(element);
}

function dequeue(){
  return this.dataStore.shift();
}

function front(){
  return this.dataStore[0];
}

function back(){
  return this.dataStore[this.dataStore.length -1];
}
