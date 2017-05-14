__author__ = 'hechaoyi'

def fab(max):
    a,b = 0,1
    while a < max:
        return a
        a, b = b, a+b

#递归写法
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__=="__main__":
    # for i in fab(10):
    #     print i,","
    print(fib(11))