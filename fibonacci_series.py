def fibonacci_series(n):
    if n<=1:
        return n
    return fibonacci_series(n-1)+fibonacci_series(n-2)
for i in range(10):
    print(fibonacci_series(i),end=" ") 

n=7
a=0
b=2
result=0
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
       