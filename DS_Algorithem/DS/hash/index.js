function HashTable() {
    this.table = new Array(37);
    this.simpleHash = simpleHash;
    this.showDistro = showDistro;
    this.put = put;
    // this.get = get;
}

/* 散列值会重复 */
function simpleHash(data) {
    var total = 0;
    for (var i = 0; i < data.length; i++) {
        total += data.charCodeAt(i);
    }
    return total % this.table.length;
}

function put(data) {
    var pos = this.simpleHash(data);
    this.table[pos] = data;
}

function showDistro() {
    var n = 0;
    for (var i = 0; i < this.table.length; i++) {
        if (this.table[i] != undefined) {
            print(i + ": " + this.table[i]);
        }
    }


    /* 一个更好的散列函数 */
    function betterHash(string, arr) {
        const H = 37;
        var total = 0;
        for (var i = 0; i < string.length; i++) {
            total += H * total + string.charCodeAt(i);
        }
        total = total % arr.length;
        return parseInt(total);
    }

    /* 散列化整型键 */
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    /* 生成学生成绩数据(用于检验哪个检测算法好) */
    function genStuData(arr) {
        for (var i = 0; i < arr.length; i++) {
            var num = "";
            for (var j = 0; j < 9; j++) {
                num += Math.floor(Math.random() * 10)；
            }
            num += getRandomInt(50, 100);
            arr[i] = num;
        }
    }

    /* 碰撞处理:开链法 */
    function buildChains() {
        for (var i = 0; i < this.table.length; i++) {
            this.table[i] = new Array();
        }
    }

    function put(key, data) {
        var pos = this.betterHash(key);
        var index = 0;
        if (this.table[pos][index] == undefined) {
            this.table[pos][index + 1] = data;
            //++index;
        } else {
            while (this.table[pos][index] != undefined) {
                ++index;
            }
            this.table[pos][index + 1] = data;
        }
    }

    function get(key) {
        var index = 0;
        var hash = this.betterHash(key);
        if (this.table[pos][index] == key) {
            return this.table[pos][index + 1
                //index += 2;
            }
            else {
                while (this.table[pos][index] != key) {
                    index += 2;
                }
                return this.table[pos][index + 1];
            }
        }

        /* 碰撞检测方法2: 线性探测法 */
        this.values = [];

        function put(key, data) {
            var pos = this.betterHash(key);
            if (this.table[pos] == undefined) {
                this.table[pos] = key;
                this.value[pos] = value;
            } else {
                while (this.table[pos] != undefined) {
                    pos++;
                }
                this.table[pos] = key;
                this.value[pos] = data;
            }
        }

        function get(key) {
            var hash = -1;
            hash = this.betterHash(key);
            if (hash > -1) {
                for (var i = 0; i < this.table[hash] != undefined; i++) {
                    if (this.table[hash] == key) {
                        return this.value[hash];
                    }
                }
                return undefined;
            }
        }
