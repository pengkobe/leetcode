function Set(){
  this.dataStore =[];
  this.add = add;
  this.remove = remove;
  this.size = size;
  this.union = union;
  this.intersect = intersect;
  this.subset = subset;
  this.difference = difference;
  this.show = show;
}

function add(data){
  if(this.dataStore.indexOf(data) < 0){
    this.dataStore.push(data);
    return true;
  }else{
    return false;
  }
}

function remove(){
  var pos = this.dataStore.indexOf(data);
  if(pos > -1){
    this.dataStore.splice(pos,1);
    return true;
  }
  else{
    return false;
  }
}

function show(){
  return this.dataStore;
}

/* 求交集*/
function intersect(set){
  var tempSet = new Set();
  for (var i = 0; i < this.dataStore.length; i++) {
    if(set.contains(this.dataStore[i])){
      tempSet.add(this.dataStore[i]);
    }
  }
  return tempSet;
}

/* 判断是否为子集*/
function difference(set){
    var tempSet = new Set();
  for (var i = 0; i < this.dataStore.length; i++) {
    if(!set.contains(this.dataStore[i])){
      tempSet.add(this.dataStore[i]);
    }
  }
  return tempSet;
}
