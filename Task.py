
#Calculator Functions
def add(a,b):
    print(a+b)
    
def difference(a,b):
    print(a-b)
    
def multiply(a,b):
    print(a*b)
    
def divide(a,b):
    print(a/b)


#Armstrong number
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
        
#Prime number
def Prime(n):
    flag=0
    for i in range(2,n//2):
        if(n%i==0):
            flag=1
    if(flag==1):
        print(n,"is not a prime number")
    else:
        print(n,"is a prime number")
        
        
#for checking odd and even
def Oddeven(n):
    if(n%2==0):
        print(n,"is an even number")
    else:
        print(n,"is an odd number")

#Factorial
def fact(n):
    if(n==1):
        return 1
    else:
        return(n*fact(n-1))
        
def Factorial(n):
    print("\nFactorial of",n,"is",fact(n))
    

#Calculator
def Calculator():
    a=int(input("\nEnter first number : "))
    b=int(input("Enter second number : "))
    op=input("Enter Operation: +,-,*,/ : ")
    if (op=="+"):
        add(a,b)
    elif(op=="-"):
        difference(a,b)
    elif(op=="/"):
        divide(a,b)
    elif(op=="*"):
        multiply(a,b)
        
        
#number fumctions
def numfunc():
    n=int(input("Enter a number"))
    print("Choose your operation from below")
    print("1. Armstrong number")
    print("2. Prime or not")
    print("3. Odd or Even")
    print("4. Factorial")
    choice=int(input(":-"))
    
    if(choice==1):
        Armstrong(n)
    elif(choice==2):
        Prime(n)
    elif(choice==3):
        Oddeven(n)
    elif(choice==4):
        Factorial(n)

#main
while(True):
    print("\n1. Binary Calculator")
    print("2. Number functions")
    print("3. Press any other key to exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        Calculator()
    elif(choice==2):
        numfunc()
    else:
        break
