# -*- coding: utf-8 -*-
# 2017-0630
# 本题难度：★★
# 两个非空链表，分别代表两个非负整数，链表的每个节点储存着整数的一位，并且是倒序储存的，将这两个数字相加返回新的链表，如：

# 输入: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 返回: 7 -> 0 -> 8
# 提示，这道题需要考虑溢出问题。

# 失误，用的数组实现
def addLinkedList(a,b):
    addflag = 0 ;
    len_a = len(a);
    len_b = len(b);
    if(len_a == len_b == 0):
        return [];
    ret = [];

    min_len = len_a if len_a < len_b else len_b;
    for i in range(min_len):
        value = a[i] + b[i];
        if addflag == 1:
            value = value + addflag;
        if value >= 10:
            addflag = 1;
            value -= 10;
        else:
            addflag = 0;
        ret.append(value);
    
    temp = a if len_a > len_b else b;
    max_len = len_a if len_a > len_b else len_b;
    for j in range(min_len, max_len):
        if addflag == 1:
             temp[j] =  temp[j] + addflag;
        if temp[j] >= 10:
            addflag = 1;
            temp[j] -= 10;
        else:
            addflag = 0;
            break;
    if addflag == 1:
        temp.append(1);
    ret = ret + temp[min_len:];
        
    return ret;

print (addLinkedList([2,4,3],[5,6,4]))
print (addLinkedList([2,4,3,9,9],[5,6,9]))


# 正解，用链表实现
def addLinkedList(linkA, linkB):
    A_len = linkA.length;
    B_len = linkB.length;
    if A_len > B_len:
        max_len = A_len
        target = linkA.head();
        plus = linkB.head();
    else:
         max_len = B_len;
         target = linkB.head();
         plus = linkA.head();

    flag = false;
    while max_len > 0:
        if flag:
            if plus == null:
                # 误区2 这里得判断 target 是否还要 next
                _sum = target.element +1;
            else:
                _sum = target.element + plus.element +1;
        else:
            if plus == null:
                _sum = target.element;
                break;
            else:
                _sum = target.element + plus.element;
        if _sum > 10:
            flag = true;
            target.element = _sum - 10;
        else:
            target.element = _sum;
        target = target.next();
        # 误区1 plus 为 null
        if plus != null:
             plus = plus.next();
            
        max_len = max_len - 1;

    return target;
        



# 胡子哥标准参考答案
# import LinkedList, {Node} from './linkedlist';

# const linkA = new LinkedList(2);
# linkA.append(4);
# linkA.append(3);

# const linkB = new LinkedList(5);
# linkB.append(6);
# linkB.append(4);

# const ret = resolve(linkA, linkB);
# console.log(JSON.stringify(ret, null, 2));

# function resolve(a, b) {
#   const alen = a.length;
#   const blen = b.length;
#   let count = Math.max(alen, blen);
#   let target = a.head, plus = b.head;
#   if (alen < blen) {
#     target = b.head;
#     plus = a.head;
#   }
#   while(count--) {
#     const sum = target.element + plus.element;
#     const bits = sum % 10;
#     const tens = ~~(sum / 10);
#     target.element = bits;
#     if (tens && !target.next) {
#       target.next = new Node(tens);
#     } else if (tens) {
#       target.next.element = target.next.element + tens;
#     }
#     target = target.next;
#　   这里有异议
#     plus = plus.next;
#   }
#   return alen < blen ? b : a;
# }


# 胡子哥标准参考答案（纠正后）
# function resolve(a, b) {
#   const alen = a.length;
#   const blen = b.length;
#   let count = Math.max(alen, blen);
#   let target = a.head, plus = b.head;
#   if (alen < blen) {
#     target = b.head;
#     plus = a.head;
#   }
#   while(count--) {
# -  const sum = target.element + plus.element;
# +  const sum = target.element + ( plus && plus.element || 0);
#     const bits = sum % 10;
#     const tens = ~~(sum / 10);
#     target.element = bits;
#     if (tens && !target.next) {
#       target.next = new Node(tens);
#     } else if (tens) {
#       target.next.element = target.next.element + tens;
#     }
#     target = target.next;
# -   plus = plus.next;
# +   plus = plus && plus.next || null;
#   }
#   return alen < blen ? b : a;
# }

# /**
#  * 单向链表的实现
#  * 
#  * @class Node
#  */
# export class Node {
#   constructor(element, next) {
#     this.element = element;
#     this.next = next;
#   }
# }

# export default class LikedList {

#   length = 0;
#   head = null;

#   constructor(element) {
#     if (element) {
#       this.head = new Node(element);
#       this.length++;
#     }
#   }

#   /**
#    * 尾部增加元素
#    * 
#    * @param {Node} element 
#    * @memberof LikedList
#    */
#   append(element) {
#     const node = new Node(element);
#     if (this.head === null) {
#       this.head = node;
#     } else {
#       let cursor = this.head;
#       while (cursor.next) {
#         cursor = cursor.next;
#       }
#       cursor.next = node;
#     }
#     this.length++;
#   }

#   /**
#    * 插入元素
#    * 
#    * @param {Node} element
#    * @param {Number} pos
#    * @returns 
#    * @memberof LikedList
#    */
#   insert(element, pos) {
#     if (pos >= 0 && pos <= this.length) {
#       const node = new Node(element);
#       this.length++;
#       if (pos === 0) {
#         node.next = this.head;
#         this.head = node;
#         return true;
#       }
#       let cur = 0;
#       let target = this.head;
#       while (pos > cur++) {
#         target = target.next;
#       }
#       node.next = target.next;
#       target.next = node;
#       return true;
#     } else {
#       return false;
#     }
#   }

#   /**
#    * 删除指定位置的元素
#    * 
#    * @param {Number} pos 
#    * @returns 
#    * @memberof LikedList
#    */
#   removeAt(pos) {
#     if (!this.length) return false;
#     if (pos >= 0 && pos < this.length) {
#       let cur = 0;
#       if (pos === 0) {
#         this.head = this.head.next;
#         this.length--;
#         return true;
#       }
#       let target = this.head;
#       while (pos - 1 > cur++) {
#         target = target.next;
#       }
#       target.next = target.next.next;
#       this.length--;
#       return true;
#     } else {
#       return false;
#     }
#   }

#   /**
#    * 查找一个元素的位置
#    * 
#    * @param {any} element 
#    * @returns 
#    * @memberof LikedList
#    */
#   indexOf(element) {
#     let target = this.head;
#     let count = 0;
#     while(target.next) {
#       if (target.element === element) {
#         return count;
#       }
#       count++;
#       target = target.next;
#     }
#     if (target.element === element) {
#       return count;
#     }
#     return -1;
#   }

#   /**
#    * remove one element
#    * 
#    * @param {any} element 
#    * @memberof LikedList
#    */
#   remove(element) {
#     const index = this.indexOf(element);
#     return this.removeAt(index);
#   }

#   /**
#    * 清空链表
#    */
#   clear() {
#     this.length = 0;
#     this.head = null;
#   }
# }