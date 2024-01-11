
    
def fibonacci(n):       
    fib_list=[]
    for i in range(n+1):
        if i==0 or i==1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list
print(fibonacci(7))