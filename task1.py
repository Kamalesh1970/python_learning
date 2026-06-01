# TASK 1

# name=input("enter your name:");
# age=int(input("enter your age:"))
# print("my name is",name)
# print("my age is",age) 


# TASK 2

# a=int(input())
# b=int(input())
# c=int(input())
# d=a*b*c
# print(d)
# e=a+b+c
# print(e)  
# print(d/e)  

# TASK 3

# name=input()
# score=int(input())
# department=input()
# print("my name is",name)
# print("my score is",score/10,"/10")
# print("my department is",department)

# TASK 4

# meghna=input()
# if(meghna=="Died"):
#     print("surya meets meghna")
# else:
#     print("surya does not meet meghna")    

# TASK 5

# marks=int(input("enter your marks:"))
# if(marks>=35):
#     print("pass")
# else:
#     print("fail")  
 

# TASK 6

# income=int(input("income:"))
# if(income>7000):
#     print(" not eligible")
# else:
#     print("eligible")

# TASK 7
# a=int(input("enter"))
# if(a%3==0 and a%5==0):
#     print("yes")
# else:
#     print("no")    

# task 8
 
# a = int(input("enter;"))
# if(a%2==0):
#     print("even")
# else:    print("odd")    
        
# TASK 9
# a=int(input("enter:"))
# if(a<35):
#     print("poor")
# elif(a>35 and a<70):
#     print("average")
# else: 
#     print("good")        

# TASK 10
# a=int(input("entera:"))
# b=int(input("enterb:"))
# if(input("add")=="add"):
#     print(a+b)
# elif(input("sub")=="sub"):
#     print(a-b)
# elif(input("mul")=="mul"):
#     print(a*b)
# elif(input("div")=="div"):
#     print(a/b)
# else:    print("invalid")      
# 
# 
# a=int(input("enter:"))
# b=int(input("enter:"))
# operation=input("enter operation:")
# if(operation=="add"):
#     print(a+b)
# elif(operation=="sub"):                   
#     print(a-b)      
# elif(operation=="mul"):
#     print(a*b)
# elif(operation=="div"):
#     print(a/b)
# else:    print("invalid")       

# TASK 11
# salary=int(input("enter salary:"))
# age=int(input("enter age:"))
# if (salary>=20000 or age<=25):
#     loan_amount=int(input("enter loan amount:"))
#     if(loan_amount>50000):
#         print("maximum loan amount is 50000")
#     else:
#         print("loan approved")    
# else:
#     print("loan not approved")        

# TASK 12
# a=int(input("entera:"))
# b=int(input("enterb:"))
# c=int(input("enterc:"))
# d=int(input("enterd:"))
# e=int(input("entere:"))
# f=(a+b+c+d+e)/5
# print("average is",f)
# if(f<35):
#     print("addition class")
# else:
#     print("good to go")    

# TASK 13
# for i in range(1,11):
#     print(i,"x9=",i*9)

# TASK 14
# a=int(input("enter:"))
# b=int(input("enter:"))
# for i in range(a+1,b):
#     print(i)

# TASK 15
# for i in range(1,11):
#     if(i%2==0):
#         print(i)

# TASK 16
# count=0
# for i in range (1,11):
#     if(i%2==0):
#         count=count+1
# print(count)

# TASK 17
# e_count=0
# o_count=0
# for i in range(1,20):
#     if(i%2==0):
#         e_count=e_count+1
#     else:
#         o_count=o_count+1
# print("even count is",e_count)
# print("odd count is",o_count)

# TASK 18
# count=0
# for i in range(1,100):
#     if(i%3==0 and i%5==0):
#         count=count+1
# print(count)        

# TASK 19
# sum=0
# for i in range(1,6):
#     sum=sum+i
# print(sum)    

# TASK 20
# a=[]
# for i in range(5):
#     num=int(input("enter num" +str(i+1)+":"))
#     a.append(num)
# print(a)   
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)     
# average=sum/ len(a)
# print(average)

# TASK 21
# n=int(input("enter:"))
# sum=0
# for i in range(1,n+1):
#     print(i,end = " ")
#     sum=sum+i
# print("\nSum:",sum)

# TASK 22
# n = int(input("enter:"))
# for i in range (1,n+1):
#     cube=i**3
#     print("number is:",i,"and the cube of",i,"is:",cube)

# TASK 23
# for i in range(1,3):
#     print("week:",i)
#     for j in range(1,4):
#         print("Day:",j)

# TASK 24
# for i in range(5):
#     print()
#     for j in range(1,i+1):
#         print("*",end="")

# for i in range(-1,0,5):
#     print("*"*i)

# for  i in range(5):
#         for j in range(i):
#                 print("",end=" ")
#         for j in range(5-i):
#                 print("*",end="")
#         print()    

# for i in range(5):
#     for j in range(5-i):
#         print("",end=" ")
#     for j in  range(i+1):
#         print("*",end="")
#     print()  

# TASK 25
# i=1
# while(i<6):
#     print(i)   
#     i=i+1
                   
# TASK 26
# i=10
# while(i<=200):
#     print(i,end=",")
#     i=i+10

# TASK 27
# i=10
# while(i>=1):
#     print(i)
#     i=i-1

# TASK 28
# i=5
# fact=1
# while(i>=1):
#     fact=fact*i
#     i=i-1
# print(fact)    

# TASK 29
# def add():
#     a=int(input("entera:"))
#     b=int(input("enterb:"))
#     print(a+b)  

# def sub():
#     a=int(input("entera:"))
#     b=int(input("enterb:"))
#     print(a-b)  

# def mul():
#     a=int(input("entera:"))
#     b=int(input("enterb:"))
#     print(a*b)

# def div():
#     a=int(input("entera:"))
#     b=int(input("enterb:"))
#     print(a/b)  

# add()
# sub()
# mul()
# div()   

# TASK 30
# a=int(input("enter:"))
# def evenorodd():
    
#     if(a%2==0):
#         print("even")
#     else:
#         print("odd")

# evenorodd()        

# TASK 31
a=int(input("enter:"))
b=int(input("enter:"))
def findrange():
    for i in range(a,b+1):
        print(i)
findrange()