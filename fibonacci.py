#dp-fibonacci
def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    ways=[0,1]
    for i in range(2,n+1):
        ways.append(ways[i-1]+ways[i-2])
    return ways[-1]

n=int(input("number : "))
print(f(n))