# # # # # # # n = int(input("Enter any number: "))
# # # # # # # if(n%2==0):
# # # # # # #     print("Even")
# # # # # # # else:
# # # # # # #     print("Odd")


# # # # # # nepali=["momo", "chauchau"]
# # # # # # indian = ["dosa", "chapati"]
# # # # # # chinese = ["noodles", "tibetian momo"]



# # # # # # ask = input("Enter the food: ")

# # # # # # if( ask in nepali):
# # # # # #     print("Nepal")
# # # # # # elif(ask in indian):
# # # # # #     print("India")
# # # # # # else:
# # # # # #     print("china"
          
# # # # # #           )


# # # # # exp=[11,22,33,22,33]
# # # # # total= 0

# # # # # for i in range(len(exp)):
# # # # #     print(f"In {i+1} month the expense is: {exp[i]}")

# # # # #     total= exp[i] + total
# # # # # print(total)


# # # # # for i in range(1,6):
# # # # #     if i %2 !=0:
# # # # #         print(f"Squre of {i} is: {i*i}")
        


# # # # # sum =0
# # # # # for i in range(1,11):
# # # # #     sum= i + sum

# # # # # print(sum)


# # # # t_l =[2,4,5,4,3]
# # # # s_l = [3,4,5,3,21,30]

# # # # def total(exp):
# # # #     total =0
# # # #     for i in exp:
# # # #         total = total + i
# # # #     return total

# # # # t_total = total(t_l)
# # # # print(t_total)

# # # # s_total = total(s_l)
# # # # print(s_total)

# # ## File read and write  in Python
# # # book={} 
# # # book["so"]={
# # #     "name" : "Sweaj",
# # #     "age": "24"
# # # }
# # # print(book["so"])


# # # import json

# # # # f=open("test.txt","w")
# # # # json.dump(book,f)


# # # s=open("test.txt","r")
# # # fl=s.read()
# # # print(fl)
# # # print(type(fl))
# # # book= json.loads(fl)
# # # print(book)
# # # print(type(book))
# # # print(book["so"]["age"])
# # # s.close()
# # # print(s.closed)


# # ## Error handling in Python
# # #x= input("Enter: " )
# # # y=input("Enter: " )

# # # try:
# # #     z=int(x)/int(y)
# # # except TypeError as e:
# # #     print("Type Error")

# # # except ZeroDivisionError as e:
# # #     print("Div Error")
    
# # # try:
# # #     print(z)
# # # except NameError:
# # #     print("Name Error")
    

# # ## Classes in Python
# # # class Human:
# # #     def __init__(self,n, o):
# # #         self.name = n
# # #         self.occupation = o

# # #     def do_work(self):
# # #         if self.occupation =="Tenis":
# # #             print(self.name, "play tenis")
# # #         elif self.occupation == "Actor":
# # #             print(self.name, "Actor")
    
# # # Tom = Human("Tom", "Actor")

# # # Tom.do_work()



## Numpy in Python

# import numpy as np



# # import time
# # import sys

# # l= range(1000)
# # print(sys.getsizeof(5)*len(l))
# # a= np.arange(1000)

# # print(a.size*a.itemsize)


# a1 = np.array([1,2,3])
# a2 = np.array([[4,5,6],[3,4,5],[5,6,7]])
# # print(a1,a2)
# # print(a1 + a2)
# # print(a1 * a2)
# # print(a1 / a2)
# # print(a1 - a2)
# print(a2.shape)

# b= np.sqrt(a2)
# print(b.astype(int))
# print(a1.dot(a2))


# import numpy as np

# a= np.array([[4,5,6],
#              [3,4,5],
#              [5,6,7]])
# c= a[0:3,0:2]
# b=c.ravel()


# a= np.arange(6).reshape(3,2)
# b= np.arange(6,12).reshape(3,2)

# # print(a)
# # print(b)

# d= np.vstack((a,b))
# print(type(d)) 

# a1= np.arange(12).reshape(3,4)
# b1 = a1 > 4
# print(b1)
# print(a1[b1])

# a = np.arange(12).reshape(3,4)

# # for row in a:
# #     #print(row)
# #     for cell in row:
# #         #print(cell)

# # for x in np.nditer(a, order ="F", flags=["external_loop"]):
# #     print(x)

# for x in np.nditer(a, op_flags=["readwrite"]):
#     x[...] = x * x
#     print(x)

# print(a)