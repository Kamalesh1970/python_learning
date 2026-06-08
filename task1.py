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
# a=int(input("enter:"))
# b=int(input("enter:"))
# def findrange():
#     for i in range(a,b+1):
#         print(i)
# findrange()

# TASK 32
# user_name="kosha"
# user_password="123456789"
# name=input()
# id=input()

# def find():
#     if(user_name==name and id==user_password):
#         print("correct")
# find()        

#  TASK 33
# a=int(input("enter:"))
# b=int(input("enter:"))
# c=int(input("enter:"))
# def add(a,b):
#     return a+b
# add=add(a,b)
# ouput=add*c
# print(ouput)

# TASK 34
# class goa:
#     name=""
#     drink=""
#     def party(self):
#         print("party in goa")
#     def dance(self):
#         print("dance in goa")
# ramesh=goa()
# suresh=goa()
# ramesh.name="ramesh"
# ramesh.drink="beer"
# print(ramesh.name ,  ramesh.drink)
# ramesh.party()
# suresh.name="suresh"
# suresh.drink="wine"
# print(suresh.name ,suresh.drink)
# suresh.dance()            

# TASK 35
# class laptop:
#     price=0
#     proc=""

# hp=laptop()
# hp.price=50000
# hp.proc="i5"
# print("hp laptop price is",hp.price)
# print("hp laptop processor is",hp.proc)

# TASK 36
# class student:
#     def __init__(self):
#         self.name=""
#         self.department=""
#     def display(self):
#         print("name is:",self.name)
#         print("department is:",self.department)
# kosha=student()    
# kosha.name="kosha"
# kosha.department="ai&ds"
# kosha.display()    

# TASK 37
# class fruit:
#     def __init__(self,color,taste):
#         self.colour=color
#         self.taste=taste
#     def display(self):
#         print("the colour of the fruit is",self.colour)
#         print("the taste of the fruit is",self.taste)
# apple=fruit("red","sweet")
# pear=fruit("green","tart")
# apple.display()
# pear.display()

# TASK 38
# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
# a=int(input("entera:"))
# b=int(input("enterb:"))
# calc=calculator(a,b)
# print("addition is",calc.add())
# print("subtraction is",calc.sub())
# print("multiplication is",calc.mul())
# print("division is",calc.div())         

# TASK 39
# class laptop:
#     chargertype="b-type"
#     def __init__(self,brand,pricr):
#         self.brand=brand
#         self.price=pricr

#     def display(self):
#         print("the brand of the laptop is",self.brand)
#         print("the price of the laptop is",self.price)
#         print("the charger type of the laptop is",self.chargertype)    
     
#     @classmethod 
#     def chandechargertype(cls):
#         cls.chargertype="c-type"    
#         print("charger type changed to",cls.chargertype)    

#     def __str__(self):
#         return f"laptop brand is {self.brand} and price is {self.price} and charger type is {self.chargertype}" 

#     @staticmethod
#     def info():
#         print("this is a laptop class")    
# hp=laptop("hp",50000)
# hp.display()
# hp.chandechargertype()
# print(hp)
# hp.info()        

# TASK 40
class grandpa():
    def phone(self):
        print("grandpa has a phone")

class father(grandpa):  
    def car(self):
        print("father has a car")

class son(father):
    def bike(self):
        print("son has a bike") 

ram=son()                        
ram.phone()
ram.car()
ram.bike()