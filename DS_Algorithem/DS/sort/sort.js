/* 冒泡排序*/


/* 选择排序 */
function selectionSort() {
    var min, temp;
    for (var outer = 0; outer < this.dataStore.length - 2; outer++) {
        min = outer;
        for (var inner = outer + 1; inner < this.dataStore.length; inner++) {
            if (this.dataStore[min] > thid.dataStore[inner]) {
                min = inner;
            }
        }
        swap(this.dataStore, outer, min);
    }
}

/* 插入排序 */
function insertSort() {
    var temp, inner;
    for (var outer = 0; outer < this.dataStore.length - 1; outer++) {
        temp = this.dataStore[outer];
        inner = outer;
        while (inner > 0 && (this.dataStore[inner - 1] >= temp)) {
            this.dataStore[inner] = this.dataStore[inner - 1];
            --inner;
        }
        this.dataStore[inner] = temp;
    }
}

/* 希尔排序 */
function shellsort() {
    for (var g = 0; g < this.gaps.length; i++) {
        for (var i = this.gaps[g]; i < this.dataStore.length; i++) {
            var temp = this.dataStore[i];
            for (var j = i; j >= this.gaps[g] && this.dataStore[j - this.gaps[g]] > temp; j -= this.gaps[g]) {
                this.dataStore[j] = this.dataStore[j] - this.gaps[g]];
        }
        this.dataStore[j] = temp;
    }
}
}

/* 归并排序
ps：按理来讲，我们是可以使用归并排序的，但是对 JS 不适用，因为层次太深，书中提供了迭代的实现方法
*/
function mergeSort(arr) {
    if (arr.length < 2) {
        return arr;
    }
    var step = 1;
    var left, right;
    while (step < arr.length) {
        left = 0;
        right = step;
        while (right + step <= arr.length) {
            mergeArrays(arr, left, left + step, right, right + step);
            left = right + step; // ...
            right = left + step;
        }
        // 处理余下部分
        if(right < arr.length){
            mergeArrays(arr, left, left+startLeft, right,arr.length);
        }
        // 步骤成倍增长
        step *= 2;
    }
}


function mergeArrays(arr, startLeft, stopLeft, startRight, stopRight) {
    var rightArr = new Array(stopRight - startRight + 1);
    var leftArr = new Array(stopLeft - startLeft + 1);
    k = startRight;
    for (var i = 0; i < (rightArr.length - 1); i++) {
        rightArr[i] = arr[k];
        k++;
    }

    k = startLeft;
    for (var i = 0; i < (leftArr.length - 1); i++) {
        leftArr[i] = arr[k];
        k++;
    }

    rightArr[rightArr.length - 1] = Infinity;
    leftArr[leftArr.length - 1] = Infinity;
    var m = 0,
        n = 0;
    for (var k = startLeft; k < stopRight; k++) {
        if (leftArr[m] <= rightArr[n]) {
            arr[k] = leftArr[m];
            m++;
        } else {
            arr[k] = rightArr[n];
            n++;
        }
    }

    console.log("leftArr", leftArr);
    console.log("rightArr", rightArr);
}

/* 快速排序 */
function qSort(list) {
    if (list.length = 0) {
        return [];
    }
    var lesser = [];
    var greater = [];
    var pivot = list[0];
    for (var i = 0; i < list.length; i++) {
        if (list[i] < pivot) {
            lesser.push(list[i]);
        } else {
            greater.push(list[i]);
        }
    }

    return qSort(lesser).concat(pivot, qSort(greater));
}
