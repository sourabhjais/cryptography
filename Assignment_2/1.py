def euclidean(a,b):
    if b==0:
        return a
    return euclidean(b,a%b)

def additive_inverse(a,b):
    if a-b < a:
        return a-b

def mutiplicative_extended(a,b):
    if euclidean(a,b)!=1:
        return
    for i in range(1, a):
        if (i * b) % a == 1:
            return i

def solution(a,c,b,n):
    if c!=0:
        b=(b+additive_inverse(n,c))%n
    d=euclidean(n,a)
    if b%d!=0:
        return
    a=a/d
    b=b/d
    x=[]
    x0=(mutiplicative_extended(n,a)*b)%n
    for i in range(0,d):
        y= x0 + i*(n/d)
        x.append(y)
    return x
a,c,b,n = [int(x) for x in input("Enter coefficient of equation: ").split()] 
print("solution are :",solution(a,c,b,n))
