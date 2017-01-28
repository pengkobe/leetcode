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
