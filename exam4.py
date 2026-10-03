#1 
# mutible va unmutible
# Ivaz shavanda va ivaz nashavanda yane list = mutible | tuple = unmutible 
# tuple asosan ivaz meshavad lekin dar memory adresash menonad!
#2
# Что такое try-except-finally
# try-except baroi ki programamon agar khatodod vayron nashavad:
# # misol
# a = int(input())
# b = int(input())
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Zero can not Division by zero")
# finally:
#     print("calculated")

#3
# list[] = yak contenyer ast ki yakchand malumot moro megirad list mutible ast va chand methud dorad sort(),revers(),count(),index(),va ghayra....
#tuple() = yak contenyer ast ki yakchand malumot moro megirad tuple unmutible ast va methud nadorad az list tez kor mekunad
#4
# Datatypes
# int = 10
# float = 10.2
# str = "hello"
# bool = True or False
#__________________________________________________________________
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(5))
#2
# add = [i for i in range(1,51) if i%3==0]
# print(add)
#3
# with open("text.txt","r") as file:
#     s =file.readlines()
#     print(len(s))
#4
# w = input().lower().replace(".","").replace(",","").replace("!","").replace("?","")
# def word(w):
#     w = w.split()
#     cnt = {}
#     for i in w:
#         cnt[i]= w.count(i)
#     return cnt
# print(word(w))
# #5
# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner= owner
#         self.balance=balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#     def withdraw(self,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Маблағ кофӣ нест")
#     def __str__(self):
#         return f"Owner: {self.owner}, Balance: {self.balance}"
# a = BankAccount("Alise",1500)
# a.deposit(500)
# a.withdraw(200)
# print(a)
#6
# def grade(filename):
#     with open(filename) as file:
#         a = file.readlines()
#     def mark(g):
#         if g >= 60:
#             return "Passed"
#         else:
#             return "Failed"
#     cnt={}
#     for i in range(len(a)):
#         a[i]=a[i].split()
#         cnt[a[i][0]] = int(a[i][1])
        
#     print(a)
#     print(cnt)
#     with open("report.txt","w") as file:
#         for n,m in cnt.items():
#             file.write(f"{n} {m} {mark(m)}\n")
# try:
#     grade("text.txt")
# except FileNotFoundError:
#     print("Not found")
#7
# from datetime import*
# def timing_decorator(func):
