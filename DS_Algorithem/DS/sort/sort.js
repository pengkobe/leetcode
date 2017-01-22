/* 冒泡排序*/

/* 选择排序 */
function selectionSort(){
  var min,temp;
  for (var outer = 0; outer < this.dataStore.length -2 ; outer++) {
       min = outer;
       for (var inner = outer + 1; inner < this.dataStore.length; inner++) {
          if( this.dataStore[min] > thid.dataStore[inner]){
            min = inner;
          }
       }
       swap(this.dataStore, outer, min);
  }
}

/* 插入排序 */
function insertSort(){
  var temp, inner;
  for (var outer = 0; outer < this.dataStore.length -1 ; outer++) {
    temp = this.dataStore[outer];
    inner = outer;
    while(inner > 0 && (this.dataStore[inner - 1] >= temp)){
      this.dataStore[inner] = this.dataStore[inner - 1];
      --inner;
    }
    this.dataStore[inner] = temp;
  }
}

/* 希尔排序 */
function shellsort(){
  for (var g = 0; g < this.gaps.length; i++) {
    for (var i = this.gaps[g]; i < this.dataStore.length; i++) {
      var temp = this.dataStore[ij;
      for (var j = i;  j >= this.gaps[g]&&this.dataStore[j-this.gaps[g]]>temp; j-=this.gaps[g]) {
        this.dataStore[j] = this.dataStore[j - this.gaps[g]];
      }
      this.dataStore[j] = temp;
    }
  }
}
