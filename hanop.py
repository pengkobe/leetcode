# 伪代码(n>=3)
# 1. x 柱子上的


def hanoi(n,x,y,z):
    if(n == 1):
        print(x,'-->',z);
    else:
        hanoi(n-1,x,z,y);
        print(x,'-->',z);
        hanoi(n-1,y,x,z);

    
