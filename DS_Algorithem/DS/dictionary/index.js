function Dictionary(){
  this.dataStore = new Array();
}

function add(key, value){
  this.dataStore[key] = value;
}

function find(){
  return this.dataStore[key];
}

function remove(){
  delete this.dataStore[key];
}

function showAll(){
  var datakeys = Array.prototype.slice.call(Object.keys(this.dataStores));
  for(var key in datakeys){
    console.log(datakeys[key] + "->" + this.dataStore[datakeys[key]]);
  }
}
function count(){
  var n = 0;
  for each(var key in Object.keys(this.dataStore)){
    ++n;
  }
  return n;
}

/* 增加排序功能 */
function showAll(){
  for each(var key in Object.keys(this.dataStore).sort()){
     console.log(datakeys[key] + "->" + this.dataStore[datakeys[key]]);
  }
}
