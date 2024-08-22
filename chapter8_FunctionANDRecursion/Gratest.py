

def gratest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    
print("Enter 3 numbers: ")
a=float(input())
b=float(input())
c=float(input())
print("Gratest number is ",gratest(a,b,c))