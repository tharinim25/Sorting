def Bubble(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
        print(*x)    
n=int(input())
x=list(map(int,input().split()))
Bubble(x)
print(*x)