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
a=int(input("enter a number"))
b=int(input("enter another number"))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)

