function Stack(){
  this.dataStore = [];
  this.top = 0;
  this.push = push;
  this.pop = pop;
  this.peek = peek;
}

function push(element){
  this.dataStore[this.top++] = element;
}

function pop(){
  return this.dataStore[--this.top];
}

function peek(){
  return this.dataStore[this.top-1];
}

function length(){
  return this.top;
}

function clear(){
  this.top = 0;
}

/* 数组间相互转换 */
function mulBase(){
  var s = new Stack();
  do{
    s.push(num % base);
    num = Math.floor(num /= base);
  }while( num > 0);
  var converted = "";
  while(s.length() > 0){
    converted += s.pop();
  }
  return converted;
}

/* 判断是否回文 */
function isPalindrome(word){
  var s = new Stack();
  for (var i = 0; i < word.length; i++) {
    s.push(word[i]);
  }
  var rword = "";
  while(s.length() > 0){
    rword += s.pop();
  }
  if(word == rword){
    return true;
  }else{
    return false;
  }
}

/* 使用栈模拟阶乘 */
function fact(n){
  var s = new Stack();
  while( n > 1){
    s.push(n--);
  }
  var product = 1;
  while(s.length() > 0){
    product += s.pop();
  }
  return product;
}

