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

function toString(){
  var retStr = "";
  for (var i = 0; i < this.dataStore.length; i++) {
    retStr = this.dataStore[i] + "\n";
  }
  return retStr;
}

function empty(){
  if(this.dataStore.length == 0){
    return true;
  }else{
    return false;
  }
}

/* 方块舞的舞伴分配问题 */

/* 使用队列对数据进行排序( 基数排序 ) */
function distribute(nums, queue, n, digit){
  for (var i = 0; i < n; i++) {
    if(digit == 1){
      queue[nums[i]%10].enqueue(nums[i]);
    }else{
      queue[Math.floor(nums[i]/10)].enqueue(nums[i]);
    }
  }
}

function collect(queues, nums){
  var i = 0;
  for (var digit = 0; digit < 10; digit++) {
    while(!queue[digit].empty()){
      nums[i++] = queues[digit].dequeue();
    }
  }
}
