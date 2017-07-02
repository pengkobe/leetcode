# 递归实现伪代码(n>=2)
# 1. x 柱子上的 n-1 盘借助 z 柱子移到 y
# 2. x 柱子移动到 z
# 3. y 上的 n-1 盘借助 x 移动到 z

def hanoi(n,x,y,z):
    if(n == 1):
        print(x,'-->',z);
    else:
        hanoi(n-1,x,z,y);
        print(x,'-->',z);
        hanoi(n-1,y,x,z);

    
# 迭代实现，基于栈

def hanoi_py(n,x,y,z):
    s=[];
    t=[n,x,y,z];
    s.append(t)
    while(len(s)>0):
        q = s[len(s)-1];
        n = q[0];  
        x = q[1];  
        y = q[2];  
        z = q[3];
        del s[len(s)-1];
        if n==1:
            print(x,'-->',z);
        else:
            s.append([n - 1, y,x,z]);
            s.append([1, x, y, z]);
            s.append([n - 1, x,z,y]);
            

# 参考1 c++
# void hanoi(int n, char x, char y, char z)  
# {  
#     std::stack<Quad> s;  
#     s.push(Quad(n, x, y, z));  
#     while (!s.empty()) {  
#         Quad q = s.top();  
#         s.pop();  
#         n = q._n;  
#         x = q._x;  
#         y = q._y;  
#         z = q._z;  
#         if (n == 1) {  
#             std::cout << "Move top disk from peg " << q._x  
#                  << " to peg " << q._z << "\n";  
#         }  
#         else {  
#             s.push(Quad(n - 1, y, x, z));  // x,z,y
#             s.push(Quad(1, x, y, z));  
#             s.push(Quad(n - 1, x, z, y));  // y,x,z
#         }  
#     }  
# } 



# 参考2 c
# #include <stdio.h>
# #include <stdlib.h>
# typedef struct hdata{
# 　　int n;
# 　　char x;
# 　　char y;
# 　　char z;
# }hdata;

# void hanluota(int n,char x,char y,char z)
# {
# 　　hdata harry[50];
# 　　char ch;　　　　　　　　//用于交换使用
# 　　int j=0;　　　　　　    //用于计数移动次数
# 　　int i=0;　　　　　　　　//始终指向栈顶
# 　　harry[i].n=n;　　　　//汉诺塔层数
# 　　harry[i].x=x;
# 　　harry[i].y=y;
# 　　harry[i].z=z;
# 　　while(1){
# 　　　　　　while(harry[i].n-1>0){　　　　//使堆栈树最左边元素入栈，直到最后一层为止
# 　　　　　　　　harry[i+1].n=harry[i].n-1;
# 　　　　　　　　harry[i+1].x=harry[i].x;
# 　　　　　　　　harry[i+1].y=harry[i].z;
# 　　　　　　　　harry[i+1].z=harry[i].y;
# 　　　　　　　　i++;
# 　　　　　　}
# 　　　　　　printf("%d:%c-->%c\n",++j,harry[i].x,harry[i].z);//使用栈顶元素

# 　　　　　　i--;　　　　　　　　//使栈顶元素退出
# 　　　　　　if(i==-1) break;　　 //如果栈空了就退出循环
# 　　　　　　printf("%d:%c-->%c\n",++j,harry[i].x,harry[i].z);//使用栈顶元素

# 　　　　　　//接下来继续使 （使用过的）栈顶元素退出并使得堆栈树右边元素入栈
# 　　　　　　ch=harry[i].x;
# 　　　　　　harry[i].x=harry[i].y;
# 　　　　　　harry[i].y=ch;
# 　　　　　　harry[i].n=harry[i].n-1;    
# 　　}
# } 

# int main(int argc, char *argv[]){
# 　　hanluota(6,'a','b','c');
# 　　return 0;
# }



            


                
           