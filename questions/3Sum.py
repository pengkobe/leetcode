# -*- coding: utf-8 -*-

# 本题难度：★★
# 给定一个整数数组 S，找到所有的三元元组 (a, b, c)，使得 a + b + c = 0，注意，

# (a, b, c) 中 a ≤ b ≤ c
# 不要输出重复的元组
# 比如：

# 给定 S = [-1, 0, 1, 2, -1, -4]，输出 [[-1, 0, 1], [-1, -1, 2]]
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/12.md



# function resolve(list) {
#     var sortedList = list.sort(function(a, b) {
#         return (a < b ? -1 : a > b ? 1 : 0)
#     })
#     var result = [], LIST_LENGTH = sortedList.length, LAST_SECOND = LIST_LENGTH - 2

#     if (LIST_LENGTH >= 3) {
#         var first = 0, second = 1, inResult = {}, computing = true

#         while (computing) {
#             var a = sortedList[first], b = sortedList[second], v = [a, b].join()

#             for (var third = second + 1; third < LIST_LENGTH; third++) {
#                 var c = sortedList[third]

#                 if ((a + b > 0) || (a + b < 0 && c > -(a + b))) break

#                 if ((a + b + c === 0) && (inResult[c] !== v)) {
#                     inResult[c] = v
#                     result.push([a, b, c])
#                 }
#             }
#             if ((first < LIST_LENGTH - 3) && (second <= LAST_SECOND)) {
#                 second = (second === LAST_SECOND) ? (++first, first + 1) : ++second
#             } else {
#                 computing = false
#             }
#         }
#     }

#     return result
# }

# console.log(resolve([-1, 0, 1, 2, -1, 4]))

# Time Limit Exceeded 
def _3Sum(array):
    if len(array) < 3:
        return [];
    def _s(x,y):
        if x < y:
            return 1;
        elif x > y:
            return -1;
        else:
            return 0;
    # 妙点 1
    array.sort(_s);
    #print(array)
    ret = [];
    first,second = 0,1;
    flag = True;
    # 妙点2
    temp = {};
    while(flag):
        a = array[first];
        b = array[second];
        for third in range(second+1,len(array)):
            c = array[third];
            # 误区1
            if a+b < 0 or (a+b > 0 and a+b < -c):
                break;
            #print(a,b,c)
            if (a+b+c) == 0 and (temp.has_key(c) == False or  temp[c] != [a,b]):
                temp[c] = [a,b]
                ret.append([c,b,a]);
       
        # 误区2
        # first = second;
        # second = second +1;
        # if second > len(array)-2 :
        #     flag = False;
        if second == len(array)-2:
            if(first == second -1):
                flag = False;
            first = first +1;
            second = first +1;
        else:
            second = second  + 1 ;
    return ret; 

print(_3Sum([-1, 0, 1, 2, -1, 4]))
print(_3Sum([0, 0, 0,0, 0, 0]))
print(_3Sum([0, 1, 1, 2, -1, -3]))
print(_3Sum([-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,
-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,
10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8]))


def _3Sum_1(array):

    while(start < end-2):
        a = array[start];
        b = array[end -1];
        temp = end -2;

        i = 0; j = temp;
        t = i;
        while ( t < j ):
            c = array[temp];
            if (a + b + c > 0):
                # 删掉第一个正数
                break;
            if (a + b + c == 0):
                ret.append([c,b,a]);
                i = temp + 1;

