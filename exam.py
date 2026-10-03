1
#неизмняемые обьекты это те обьекты которые при попытка изменение , python лишь создает  другой новый обьект в памяти и изменяеть путь к новым обьектам , в таком случае старый обьект остается в памяти до завершение программы  
# 
# B2  внутри try пишется код , если возникли ошибки во время выполнения то exept не дает программу закончится с ошибкой , а finally работает в любом случае , если коротко try except помогает ,поймать ошибки и не позволяет программу рухнут из за ошибки 

# B3 tuple это неизменяемый обьект и его нельзя изменить после создания , list это изменяемый и у него есть такие методы как append(), remove() для работы с элементами внутри 
# tuple лучше использовать для безопасное хранение данных

# B4 перменные это  коробки которые содержать данные , они могут хранить такие данные как:
# int = только натуральные цифры
# float = дробные цифры
# str = только строки
# bool =  только True(1) или False(0)
# list,dict и т.д

2
# ==== B5 ====

# def fibonacci(n):
#     if n <= 0:
#       return []
#     if n == 1:
#       return [0]    
#     result = [1, 1]
#     for i in range(2, n):
#       result.append(result[-1] + result[-2])    
#     return result[:n]

# print(fibonacci(10))







# ==== B6 ====
# evens = [ i for i in range(1,51) if i%3 == 0]
# print(evens)

# ==== B7 ====
# with open("text.txt") as file:
#     f = file.readlines()
#     print(len(f))


3
# word = input().lower().replace(".","").replace(",","").replace("!","").replace("?","")

# def word_count(word:str):
#     word = word.split()
#     count = {}
#     for words in word:
#         count[words] = word.count(words) 
#     return count

# print(word_count(word))

# ==== B9 ====
# class BankAccount:

#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,amount):
#         if amount >0:
#             self.balance += amount
#     def withdraw(self,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Недостаточно средств")
#     def __str__(self):
#         return f"Owner: {self.owner}, Balance: {self.balance}"

# card = BankAccount("Alice", 1000)
# card.deposit(500)
# card.withdraw(2000)
# print(card)
        

4
# ==== B10 ====
from datetime import*

def timing(func):
    def inner(*args, **kwargs):
        m = datetime.now()
        now = datetime.now()
        snow =now.strftime("%S")
        msnow = now.strftime("%s")
        func(*args)
        then = datetime.now()
        ths = then.strftime("%S")
        mthen = then.strftime("%s")
        print(f"Spent time: {int(ths)-int(snow)}-seconds and {int(mthen)-int(msnow)}")
    return inner





@timing
def count():
    res = 0
    for i in range(1,10000000):
        res += i
    print(res)

count()





# def grades(filename):
#     with open(filename) as file:
#         lines = file.readlines()
#     def status(grade):
#         if grade >= 60:
#             return "Passed"
#         elif grade < 60:
#             return "Failed"
#     sums = {}
#     for i in range(len(lines)):
#         lines[i] = lines[i].split()
#         sums[lines[i][0]] = int(lines[i][1])
   

#     with open("report.txt", "w") as file:
#         for k,v in sums.items():
#             file.write(f"{k} {v} {status(v)}\n")
# try:
#     grades("students.txt")
# except FileNotFoundError:
#     print("File not found!")