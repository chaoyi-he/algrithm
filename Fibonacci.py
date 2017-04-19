__author__ = 'hechaoyi'

def fab(max):
    a,b = 0,1
    while a < max:
        return a
        a, b = b, a+b


if __name__=="__main__":
    for i in fab(10):
        print i,","