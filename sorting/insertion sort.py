def Insertion(x):
    for i in range(1,len(x)):
        temp=x[i]
        j=i-1
        while j>=0 and temp<x[j]:
            x[j+1]=x[j]
            j=j-1
        x[j+1]=temp
x=list(map(int,input().split()))
Insertion(x)
print(x)