def add(a,b):
    print(a+b)
def sub(a,b):
    sub=0
    if a>b:
        print(a-b)
    else:
        print(b-a)
def mul(a,b):
    print(a*b)
def div(a,b):
    div = 0
    if a>b:
        div = a/b
    else:
        div = b/a
    print(div)
def gcd(a,b):
    while(b):
        a,b=b,a%b
    print(a)
def ss(a,b):
    ss=0
    ss=(a*a)+(b*b)
    print(ss)
a=int(input("enter a number"))
b=int(input("enter another number"))

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
gcd(a,b)
ss(a,b)
