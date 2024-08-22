def fun1():
    print("Good day")


fun1()

def fun2(name):
    n="Hello "+name
    return n

print(fun2("Prem"))

#default value function
def fun3(name="hari"):
    n="Hello "+name
    return n

print(fun3())
print(fun3("Prem"))




