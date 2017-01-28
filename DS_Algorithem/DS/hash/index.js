function HashTable(){
  this.table = new Array(37);
  this.simpleHash = simpleHash;
  this.showDistro = showDistro;
  this.put = put;
  // this.get = get;
}

/* 散列值会重复 */
function simpleHash(data){
  var total = 0;
  for (var i = 0; i < data.length; i++) {
     total += data.charCodeAt(i);
   }
   return total % this.table.length;
}

function put(data){
  var pos = this.simpleHash(data);
  this.table[pos] = data;
}

function showDistro(){
  var n = 0;
  for (var i = 0; i < this.table.length; i++) {
    if(this.table[i] != undefined){
      print(i + ": " + this.table[i]);
    }
}


/* 一个更好的散列函数 */
function betterHash(string, arr){
  const H =37;
  var total = 0;
  for (var i = 0; i < string.length; i++) {
    total += H * total + string.charCodeAt(i);
  }
  total = total % arr.length;
  return parseInt(total);
}
