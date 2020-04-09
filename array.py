from numpy import *
from threading import *
from time import sleep





# def binarysearch(lst,n):
#     a= 0
#     b=len(lst)-1
#
#     for num in lst:
#         num = floor((a + b) / 2)
#         if  num==n:
#             print('found ')
#             break
#         else:
#             if num<n:
#                 a=num
#             else:
#                 b=num
#     else:
#         print('not found')
# list=[2,10,5,8,9,12,13,3,56,987,6543,8765,7654,76,34,678,89]
# list.sort()
# n=int(input('which number u want to search '))
# binarysearch(list,n)


# def search(lst,n):
#     i=0
#     for num in lst:
#         i = i + 1
#         if num==n:
#
#             print('found in {} position'.format(i-1))
#             break
#
#     else:
#         print('not found')
# list=[2,3,5,8,9]
# n=int(input('which number u want to search '))
# search(list,n)











# class a(Thread):
#     def call1(self):
#         for i in range(5):
#             print('hello')
#             sleep(1)
# class b(Thread):
#     def call2(self):
#         for i in range(5):
#             print('Belal')
#             sleep(1)
# o1=a()
# o2=b()
# o1.call1()
# sleep(0.2)
# o2.call2()
# o1.join()
# o2.join()
# print('bye')


# a=10
# def printfunc(p):
#     print('hello')
#     def pri():
#         p=7
#         return p
#     return pri
# printfunc(a)



# i = 1
# def recursion(a):
#     global i
#     i = i + 1
#    # print("mehedi ",i)
#     return recursion(5)
# b=7
# print(recursion(b))



# def factorial(n):
#     res=1
#     for i in range(1,n+1):
#         res=res*i
#     return res
# print(factorial(3))


# def fibo(n):
#     a,b=0,1
#     if n==1:
#         print(a)
#     elif n<0 or n==0:
#         print("Invalid number")
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n,1):
#             c=a+b
#             if c>=100:
#                 break
#             print(c)
#
#             a,b=b,c
# fibo(39)




# arr1 = []
# arr2 = []
# def evenodd(array):
#     for i in array:
#         if i%2==0:
#             arr1.append(i)
#         else:
#             arr2.append(i)
#     return arr1, arr2
# arr=arange(1,101,1)
# print('numbers are {}'.format(arr))
# evenodd(arr)
# print('even numbers are ',arr1)
# print('odd numbers are ',arr2)






# a,b,c=10,77,88
# def details(name, **arg):
#     global b,c
#     b,c=33,44
#     a=19
#     print(a)
#     x=globals()['a']
#     print(x,a)
#     globals()['a']=20
#     print(a)
#     for i,j in arg.items():
#         print(i,j)
# details('Navin', age=15,city='berlin', mobile=123141)
# print(a,b,c)


# def update(x):
#     x.append('q')
#     print('function ',x)
# a=[10,20,30]
# update(a)
# print('main ',a)

# arr1= array([
#     [1,2,3,4],
#     [6,7,8,9],
#     [3,4,6,7]
#     ])
# m= matrix(arr1)
# m1=matrix('1 2 3 4 ; 6 7 8 0')
# print(m)
# print(m1)
# print()



# val=array('i',[1,3,6,9])
# val2=array(val.typecode,(a*a for a in val))
# print(val2)

# arr1=arange(1,10,2)
# arr2=arange(10,20,2)
# arr4=arange(10,20,2)
# arr3=arr1+ arr2+ arr4
# print(concatenate([arr1,arr2]))



# len=int(input("Enter the length of array "))
# for num in range(len):
#     a= int(input("Enter the next value "))
#     arr.append(a)
# print(arr)
# k= int(input("which element do u want to search"))
# print(arr.index(k))
# j=0
# for i in arr:
#     if i==k:
#         print(j)
#         break
#     j+=1
#


# list=[]
# len= int(input("size if th array "))
# for num in range(len):
#    a= input("enter next value ")
#    list.append(a)
# print(list)
# k= int(input("which element do u want to search"))
# print(list.index(k))
# j=0
# for i in list:
#     if i==k:
#         print(j)
#         break
#     j+=1


