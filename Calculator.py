#write a program to find the simple caluculation
def add(a,b):
    c = a+b
    return "The sum of {} and {} is {}".format(a,b,c)
def sub(a,b):
    c = a-b
    return "The difference of {} and {} is {}".format(a,b,c)
def mul(a,b):
    c = a*b
    return "The product of {} and {} is {}".format(a,b,c)
def div(a,b):
    try:
        c = a/b
        return  "The Quotient of {} and {} is {}".format(a,b,c)

    except ZeroDivisionError:
        return "Division with zero can't be performed"
    finally:
        pass
a= int(input("enter a value:"))
b= int(input("enter b value:"))
operation = input("enter add, sub,mul,div:").lower()
if operation == 'add':
    print(add(a,b))
elif operation == 'sub':
    print(sub(a,b))
elif operation == 'mul':
    print(mul(a,b))
elif operation == 'div':
    print(div(a,b))

else :
    print("Please enter a valid operation")



