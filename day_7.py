#predefine module
# import math
# print(math.sqrt(16))
# print(math.pi)




#predefine module
# import math
#  print(math.sqrt(16))
#  print(math.pi)


#  from math import *
#  print(int(sqrt(4)))
#  print(ceil(10.1))
#  print(floor(10.1))
#  print(fabs(-10.6))
#  print(fabs(10.6))


#random module:
#this module defines sevaral functions to generate
#random numbers.
#we cn use these function while develop[ing  games

# from random import *
# for i in range(5):
#     print(random())



# to generate random integer between two given
# numbwers(inclusive)

# from random import *
# for i in range(5):
#     print(randint(1,10000))





#choice() function:
#it wont return random number
#it wont return random object from the given list on tuple
# from random import *
# list=["prashnt","rahu","ashish","sandip","sunil","nikuu"]
# for i in range (10):
#     print(choice(list))



# def welcome(fname ,lname):
#     print("Hello, "+fname)
#     print("Hello, "+lname)

# def login(username,password):
#     if (username==password):
#         print("You have login successfully")
#     else :
#         print("You have entered wrong username and password")

# def square(num):
#     print("square of two no=",num*num)

# pi = 3.141592653589793





# import module1
# module1.square(4)
# module1 .login("admin","admin")
# print(module1.pi)


#third way to import a specific func /var/class/etc
# from module1 import pi,square,login ,welcome
# print(pi)
# square(4)
# login('user','user')
# welcome('Sandhya','Regate')


# from module1 import pi,square,login ,welcome
# square(4)
# login('Sandhya','Regate')
# print(Pi)
# welcome('abc','abc')




# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1])



# def func(value,values):
#     var = 1
#     values[0]=44
# t=3
# v=[1,2,3] #44
# func(t,v)
# print(t,v[0])


# arr=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# def f(i,values=[]):
#     values.append(i)
#     print(values)
    #return values
# f(1)
# f(2)
# f(3)



# fruit_list1= ['Apple','Berry','cherry','papaya']
# fruit_list2 =fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0]='Guava'
# fruit_list3[1] = 'Kiwi'
# sum=0
# for ls in (fruit_list1,fruir_list2,fruits_list3):
#     if ls[0] =='Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)

arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1] = arr[i]
for i in range(0,6):
    print(arr[i],end="")


