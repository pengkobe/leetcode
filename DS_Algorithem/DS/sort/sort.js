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
