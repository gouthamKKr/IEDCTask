def add(a,b):
    print(a+b)
    
    
def difference(a,b):
    print(a-b)
    
def multiply(a,b):
    print(a*b)
    
def divide(a,b):
    print(a/b)

def Armstrong(n):
    n1=0;
    num=n
    
    while num>0:
        rem=num%10
        n1+=rem**3
        num//=10
    
    if n1==n:
        print(n,"is a armstrong number")
    
    else:
        print(n,"is not an armstrong number")

def Prime(n):
    i=-1;
    while(++i<n/2):
        if(n%i==0):
            break
    if(i<n/2):
        print("\n",n,"is not a prime number")
    else:
        print("\n",n,"is a prime number")

def Oddeven(n):
    if(n%2==0):
        print("\n",n,"is an even number")
    else:
        print("\n",n,"is an odd number")

def fact(n):
    if(n==1):
        return 1
    else:
        return(n*fact(n-1))
        
def Factorial(n):
    print("\n Factorial of",n,"is",fact(n))
    

        
def calculator():
    a=int(input("\nEnter first number : "))
    b=int(input("\nEnter second number : "))
    op=input("Enter Operation: +,-,*,/ : ")
    if (op=="+"):
        add(a,b)
    elif(op=="-"):
        difference(a,b)
    elif(op=="/"):
        divide(a,b)
    elif(op=="*"):
        multiply(a,b)

def numfunc():
    n=int(input("\nEnter a number"))
    print("\nChoose your operation from below")
    print("\n1. Armstrong number")
    print("\n2. Prime or not")
    print("\n3. Odd or Even")
    print("\n4. Factorial")
    choice=int(input(":-"))
    
    if(choice==1):
        Armstrong(n)
    elif(choice==2):
        Prime(n)
    elif(choice==3):
        Oddeven(n)
    elif(choice==4):
        Factorial(n)

while(True):
    print("\n1. Binary Calculator\n")
    print("2. Number functions\n")
    print("3. Press any other key to exit\n")
    choice=int(input("Enter your choice"))
    if(choice==1):
        Calculator()
    elif(choice==2):
        numfunc()
    else:
        break
