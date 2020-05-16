##############  python basic (part-1)  ###############

# 1
# print('twincle twincle little star'
#       '\n\thow i wonder what u are'
#       '\n\t\tup above the world so high'
#       '\n\t\tlike a dimond in the sky'
#       '\ntwincle twincle little star')

# 2
# import sys
# print('python version '+ sys.version, sys.version_info)

# 3
# from datetime import datetime
# print('current date and time: ', datetime.now())

# 4
# from math import pi
# def circlearea(r):
#     area=pi * r *r
#     print('area of circle  with radius {} is {}'.format(r,area))
# r=float(input('enter the radius '))
# circlearea(r)

# 5
# fn=input("enter first name: ")
# ln=input("enter last name: ")
# print(f'by swapping your name:{ln} {fn} ')

# 6
# data=str(input('enter sequence of number '))
# val=data.split(',')
# list=list(val)
# tuple=tuple(val)
# print('List: {}'.format(list))
# print(f"Tuple: {tuple}")

# 7
# fname=str(input('give your file name: '))
# s=fname.split('.')
# print(f'extension of file name is {s[1]}')
# or
# fname=str(input('give your file name: '))
# if '.' in fname:
#     index= fname.index('.')
#     index+=1
#     print(f'extension is {fname[index:]}')
# else:
#     print('dont trick me')


# 8
# color_list = ["Red","Green","White" ,"Black"]
# print(f'first color  is {color_list[0]}\nlast color is {color_list[-1]}')

# 9
# str= input('give exam date: ')
# str=str.replace(',','/')
# print(f'exam date: {str}')
# or
# exam_st_date = (11,12,2014)
# a,b,c=exam_st_date
# print('The examination will start from : {} /{} /{}'.format(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
# print(f'The examination will start from : {a} /{b} /{c}')

# 10
# n=int(input('the value of n  '))
# n1=str(n)
# n2=int('{}{}'.format(n1,n1))
# n3=int(n1+n1+n1)
# print(n+n2+n3)

# 11
# print(abs(-5))

# 12
# import calendar
# print(calendar.month(2020,4))

# 13
# print('a string that you "don\'t" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> example'

# 14
# from datetime import *
# date1=date(2020,4,11)
# date2=date(1995,10,21)
# print('my age is {}'.format(date1-date2))

# 15
# pi = 3.1415926535897931
# r= 6.0
# V= (4/3)*pi* r**3
# print('The volume of the sphere is: ',V)

# 16
# num=int(input('enter any number '))
# if num<=17:
#     diff=abs(17-num)
#     print(f'difference is {diff}')
# else:
#     diff = abs(17 - num) *2
#     print(f'double difference is {diff}')

# 17
# num=int(input('enter any number '))
# if num>=100 and num<=1000:
#     print('number is within 1000')
# elif num>=100 and num<=2000:
#     print('number is within 2000')
# else:
#     print('invalid input')


# 18
# num1=int(input('enter numbers '))
# num2=int(input('enter  numbers '))
# num3=int(input('enter  numbers '))
# if num1==num2==num3:
#     print(3*(num1+num2+num3))
# else:
#     print(num1+num2+num3)

# 19
# str=str(input('enter any string '))
# if str[:2]=='Is':
#     print(f'{str}')
# print('Is',str)

# 20
# str=str(input('enter any string '))
# num=int(input('enter numbers '))
# for i in range(num):
#     print(str)

# 21
# def evenodd(x):
#     if x%2==0:
#         print('even')
#     else:
#         print('odd')
# evenodd(1)
# evenodd(0)
# evenodd(-1)
# evenodd(12)

# 22
# def count(list):
#     i = 0
#     for num in list:
#         if num == 4:
#             i += 1
#     return i
# print(count([2, 3, 4, 5, 6, 4]))
# print(count([2, 3, 5, 6]))
# print(count([2, 3, 4, 5, 6, -4]))

#23
# str=str(input('enter any string '))
# num=int(input('enter number '))
# str=str[:num]
# str= num*str
# print(str)

#24
# str=str(input('enter any string '))
# if str in 'aeiouAEIOU':
#     print('vowel')
# else:
#     print('not vowel')

#25
# def check(list,n):
#     if n in list:
#         print(f'{n} is inside {list}')
#     else:
#         print(f'{n} is not inside {list}')
# check([1,2,3,4,5,],5)
# check([1,2,3,4,5,],10)

#26
# list=[1,2,3,4,8,6]
# num=0
# for i in list:
#     print('@'*list[num])
#     num+=1


#27
# print('enter list number ')
# list=[]
# str=''
# for i in range(5):
#     str=input()
#     list.append(str)
# print(list)

#list=[1,2,31,'h']
# i=0
# s=''
# while i<4:
#     s=s+str(list[i])
#     i=i+1

#28
# numbers1 = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# numbers=[]
# for i in numbers1:
#     if i%2==0:
#         if i>=237:
#             continue
#         else:
#             numbers.append(i)
# print(numbers)

#29
# a={}
# clist1={'white','red','green'}
# clist2={'white','red'}
# print(clist1.difference(clist2))

#30
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
# area = b*h/2
# print("area = ", area)

#31
# num1=int(input('enter number 1  '))
# num2=int(input('enter number 2  '))
# gcd=1
# for i in range(max(num1,num2),0,-1):
#      if num1%i==0 and num2%i==0:
#         gcd=i
#         break
# print(f'gcd is {gcd}')

#32
# num1=int(input('enter number 1  '))
# num2=int(input('enter number 2  '))
# lcd=1
# for i in range(max(num1,num2),num1*num2):
#      if i%num1==0 and i%num2==0:
#         lcd=i
#         break
# else:
#     lcd=num1*num2
# print(f'lcd is {lcd}')

#33
# def sum(a,b,c):
#     if a==b or a==c:
#         return 0
#     elif b==c or b==a:
#         return  0
#     elif c==a or c==b:
#         return 0
#     else:
#         return a+b+c
# print(sum(1,2,3))
# print(sum(1,2,2))
# print(sum(1,2,1))
# print(sum(1,-2,2))

#34
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
#
# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(8, 12))

#35
# num1=int(input('enter number 1  '))
# num2=int(input('enter number 2  '))
#
# def returnfunc():
#     if num1==num2 or num1+num2==5 or abs(num1-num2)==5:
#         return True
#     else:
#         return False
# print(returnfunc())

#36
# def calc(num1,num2):
#     if type(num1)== int and type(num2)==int:
#         print(num1+num2)
#     else:
#         print('wrong input')
# calc(3,4)
# calc(3,'d')

#37
# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#
# personal_details()

#38
# x, y = 4, 3
# result = x * x + 2 * x * y + y * y
# print("({} + {}) ^ 2) = {}".format(x, y, result))

#39
# amt = 10000
# int = 3.5
# years = 7
#
# future_value  = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))

#40
# from math import *
# # x1,y1=[int(x) for x in input('enter (x1,y1)= ').split(',')]
# # print(x1,y1)
# # x2,y2=[int(x) for x in input("Enter x2 and y2 :").split()]
# # diff=sqrt((x1-x2)**2+(y1-y2)**2)
# # print(diff)

#41
# from os import path
# open('data', 'r')
# print(path.isfile('data'))

#42
# import sys
# print(sys.version)

#43
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

#44
# import site
# print(site.getsitepackages())

#45
# from subprocess import call
# call(["ls", "-l"])

#46
# import os
# print("Current File Name : ",os.path.realpath(__file__))

#47
# import multiprocessing
# print(multiprocessing.cpu_count())

#48
# n = "246.2458"
# print(float(n))
# print(int(float(n)))

#49
# import os
# d = os.getcwd()
# for i in os.listdir(d):
#     print(i)

#50
# for i in range(0, 10):
#     print('*', end="")
# print("\n")

#51
# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

#55
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#57
# import time
# def sum_of_n_numbers(n):
#     start_time = time.time()
#     print(start_time)
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     end_time = time.time()
#     print(end_time)
#     return s,end_time-start_time
#
# n = 5
# print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


#65
# def time(sec):
#     day=sec//86400
#     sec = sec % 86400
#     hour=sec//3600
#     sec = sec % 3600
#     min=sec//60
#     sec=sec%60
#     return day, hour,min,sec
# print(time(86399))

#68
# def sum(a):
#     arr=str(a)
#     sum =0
#     i=0
#     while i<len(arr):
#         sum=sum+int(arr[i])
#         i+=1
#     return sum
# print(sum(123))

#69
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))
#
# a1 = min(x, y, z)
# a3 = max(x, y, z)
# a2 = (x + y + z) - a1 - a3
# print("Numbers in sorted order: ", a1, a2, a3)

#72
# import math
# print(dir(math))

#79
# import sys
# str1=str(input())
# print(str(sys.getsizeof(str1)))

#81
# list_of_colors = ['Red', 'White', 'Black']
# colors = ''.join(list_of_colors)
# print(colors)

#84
# def counter(str):
#     return str.count('e')
# print(counter('erwfdeee'))

#87
# import os
# size=os.path.getsize('data')
# print(size)

#95
# a='13edfvw'
# try:
#     b=float(a)
#     print(b)
# except ValueError:
#     print('its not numeric')

#98
# import time
# print(time)
# print(time.ctime())

#110
# list1=[3,6,2]
# result= list(filter(lambda x: (x%5==0),list1))
# print(result)

#115
# from functools import reduce
# list1=[3,6,2]
# result= reduce(lambda x,y: x*y,list1)
# print(result)

#128
# print(any(x.islower() for x in input('Enter a string: ') ))

#134
# x,y= [int(x) for x in input('enter numbers: ').split()]
# print(x,y)

#140
# x=12
# print(format(x,'08b'))

#145
# def test(a):
#     print(type(a))
# test([1,2,3])
# test({1,2,3})
# test((1,2,3))

#148
# def largesmall(x):
#     l=x[0]
#     s=x[0]
#     for num in x:
#         if num>l:
#             l=num
#         if num<s:
#             s=num
#     return f'large {l} ,small {s}'
# print(largesmall([2,4,1,7,4,8,99]))

##############  python basic (part-2)  ###############

#1
# def lencheck(l1,l2):
#     if len(l1)==len(l2):
#         return  True
#     else:
#         return False
# print(lencheck([1,2,3],[1,2,3]))

#2
# import random
#
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))
#or
# import random
# char = ["a","b","c","R"]
# lenth = 5
# print(''.join(random.choice(char) for i in range (lenth)))
#or
# import itertools
# vowels = 'aeiou'
# result = []
# for item in itertools.permutations(vowels):
#     result.append("".join(item))
# for i in result:
#     print(i)

#4
# from itertools import combinations
# def threesumzero(li):
#     new=[]
#     for num in combinations(li,3):
#         if suma(num)==0:
#             new.append(num)
#         else:
#             continue
#     return new
# def suma(num):
#     return sum(num)
#
# print(threesumzero([1,4,-2,-2,6,-4]))

#5
# from random import choice
# a=range(10)
# num=choice(a)
# combo=str(num)*3
# print(combo)

#6
# def repeat(l):
#     l=list(l.split())
#     c = -1
#     for num in l:
#         c += 1
#         if l.count(num) > 1:
#             if num in l[:c]:
#                 continue
#             else:
#                 print(f'{num} is {l.count(num)} times')
# string_words = '''United States Declaration of Independence
# From Wikipedia, the free encyclopedia
# The United States Declaration of Independence is the statement
# adopted by the Second Continental Congress meeting at the Pennsylvania State
# House (Independence Hall) in Philadelphia on July 4, 1776, which announced
# that the thirteen American colonies, then at war with the Kingdom of Great
# Britain, regarded themselves as thirteen independent sovereign states, no longer
# under British rule. These states would found a new nation – the United States of
# America. John Adams was a leader in pushing for independence, which was passed
# on July 2 with no opposing vote cast. A committee of five had already drafted the
# formal declaration, to be ready when Congress voted on independence.
#
# John Adams persuaded the committee to select Thomas Jefferson to compose the original
# draft of the document, which Congress would edit to produce the final version.
# The Declaration was ultimately a formal explanation of why Congress had voted on July
# 2 to declare independence from Great Britain, more than a year after the outbreak of
# the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
# Second Day of July 1776, will be the most memorable Epocha, in the History of America."
# But Independence Day is actually celebrated on July 4, the date that the Declaration of
# Independence was approved.
#
# After ratifying the text on July 4, Congress issued the Declaration of Independence in
# several forms. It was initially published as the printed Dunlap broadside that was widely
# distributed and read to the public. The source copy used for this printing has been lost,
# and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
# with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
# by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
# is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
# popularly regarded as the official document. This engrossed copy was ordered by Congress on
# July 19 and signed primarily on August 2.
#
# The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
# The Declaration justified the independence of the United States by listing colonial grievances against
# King George III, and by asserting certain natural and legal rights, including a right of revolution.
# Having served its original purpose in announcing independence, references to the text of the
# Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
# (as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
# on human rights, particularly its second sentence:
#
# We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
# Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.
#
# This has been called "one of the best-known sentences in the English language", containing "the most potent
# and consequential words in American history". The passage came to represent a moral standard to which
# the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
# Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
# through which the United States Constitution should be interpreted.
#
# The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
# being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
# (modern-day Belgium). It also served as the primary model for numerous declarations of independence across
# Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
# 19th century.'''
# repeat(string_words)

#7
#str=open('data','r')
# str='yfmdtns dtsrnatbe srahebtgrv srbtaevsssssssssssssssssss'
# def repeat(l):
#     l=list(l)
#     c = -1
#     for num in l:
#         c += 1
#         if l.count(num) > 1:
#             if num in l[:c]:
#                 continue
#             else:
#                 print(f'{num} is {l.count(num)} times')
# repeat(str)

#8
# import bs4
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen
#
# news_url="https://news.google.com/news/rss"
# Client=urlopen(news_url)
# xml_page=Client.read()
# Client.close()
#
# soup_page=soup(xml_page,"xml")
# news_list=soup_page.findAll("item")
# # Print news title, url and publish date
# for news in news_list:
#   print(news.title.text)
#   print(news.link.text)
#   print(news.pubDate.text)
#   print("-"*60)


#9
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# for m in installed_packages_list:
#     print(m)

#10
# from itertools import combinations
# from random import choice
# sum=70
# for num in range(sum):
#   if combinations(num)==sum:
#     print(num)

#11
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# list=([(x, y, z) for x in X for y in Y for z in Z if x + y + z == 70])
# for num in list:
#   print(num)

#20
# num=int(input('give a number:  '))
# fact=1
# for i in range(num):
#     i+=1
#     fact=fact*i
# fact=str(fact)
# w= fact.count('0')
# print(w)


#21
# def notes(num):
#     notes=[500,200,100,50,20,10]
#     count=0
#     for i in notes:
#         a=int(num/i)
#         q=int(num%i)
#         num=q
#         count+=a
#     return count
# print(notes(380))
# print(notes(1300))
# print(notes(1090))DIGITSUM(123)

#23
# def DIGITSUM(x):
#     x=str(x)
#     y=sum([int(i) for i in x])
#     return y
# print(DIGITSUM(123))

#24
# def divisor(x):
#     a=[]
#     for i in range(1,x+1):
#         if x%i==0:
#             a.append(i)
#         else:
#             continue
#     if len(a)%2==0:
#         print('even')
#     else:
#         print('odd')
# divisor(12)

#25
# def mobilenumber(x):
#     p=set(str(x))
#     a={'0','1','2','3','4','5','6','7','8','9'}
#     return list(a-p)1
# print(mobilenumber(1789377471))

#29
# a=[1,2,4,6,8]
# b=[2,0,5,8,9]
# print(list(set(a)& set(b)))

#30
# def palindrome(x):
#     x=str(x)
#     a=x+x[::-1]
#     print(a)
# palindrome('erf')
# palindrome(1234)

#32
# print('enter the heights:  ')
# h=[int(input()) for i in range(8)]
# h.sort()
# print(h[:4:-1])

#33
# def sumtwonumber(x,y):
#     sum=x+y
#     return len(str(sum))
# print(sumtwonumber(10,150))

#38
# def prime(x):
#     a=[]
#     for i in range(2,x):
#        for j in range(2,i):
#            if i%j==0:
#                break
#        else:
#            a.append(i)
#     return a
# print(prime(30))

#41
# print("Input first integer:")
# x = int(input())
# print("Input second integer:")
# y = int(input())
# if x >= 10 ** 5 or y >= 10 ** 5 or x + y >= 10 ** 5:
#     print("Overflow!")
# else:
#     print("Sum of the two integers: ",x + y)

#42
# num=list(map(int,(input().split())))
# num.sort()
# num.reverse()
# print(num)

#47
# text = 'Thank you for your comment and your participation.'
# text = text.strip('.')
# text = text.split(' ')
#
# list_of_counts = list(map(lambda x: text.count(x), text))
# length_of_words = list(map(lambda x: len(x), text))
# freq = [x for x in text if text.count(x) == max(list_of_counts)]
# length = [x for x in text if len(x) == max(length_of_words)]
#
# print(f'Most frequently used: {set(freq)}', f'Maximum number of letters:{set(length)}', sep='\n')


##############  string ###############

#1
# a='jyrnhtb'
# print(len(a))

#2
# str = "google.com"
# my_count = {c:str.count(c) for c in str}
# print(my_count)

#3
# def stradd(s):
#     if len(s)>=4:
#         return s[0:2] + s[-2::1]
#     else:
#         return f'invalid input'
# print(stradd('wggfdeferfa'))

#5
# def swapstring(a,b):
#     a=list(a)
#     b=list(b)
#     temp=a[0:2]
#     a[0:2]=b[0:2]
#     b[0:2]=temp
#     print(a+b)
# swapstring('gfdg','rgege')

#7
# def not_poor(str):
#     loc1=str.find('not')
#     loc2=str.find('poor')
#     if loc1<loc2 and loc1>0 and loc2>0:
#         str = str.replace ( str [ loc1 :loc2 + 4 ] , 'good' )
#         return str
#     else:
#         return str
# print(not_poor('The lyrics is not that poor!'))
# print(not_poor('The lyrics is poor!'))

#8
# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     print(word_len)
#     word_len.sort()
#     print(word_len)
#     return word_len[-1][-1]
# print(find_longest_word(["PHP", "Exercises", "Backend"]))


#9
# def strremove(s,n):
#         return s[:n]+s[n+1:]
# print(strremove('belalethngbvqqqqq',12))

#11
# def strremove(s):
#     ns=''
#     for i in s:
#         if s.index(i)%2==0:
#             ns=ns+i
#         else:
#             continue
#     return ns
# print(strremove('belal'))

#12
# def strcount(s):
#     s=s.split()
#     a=[]
#     for i in s:
#         a.append((s.count(i),i))
#         if s.count(i)>1:
#             s.remove(i)
#     return a
# print(strcount('jbasdf aefj qwefrb qwefvb aefj'))

#13
# items = ['1','2','3']
# items=','.join(sorted(items))
# print(items)

#15
# def add_tags(tag, word):
# 	return f"<{tag}>{word}</{tag}>"
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))

#24
# a='133'
# print(a.startswith('13'))

#26
# from textwrap import *
# sample_text='''
# Python is a widely used high-level, general-purpose, interpreted,
# dynamic programming language. Its design philosophy emphasizes
# code readability, and its syntax allows programmers to express
# concepts in fewer lines of code than possible in languages such
# as C++ or Java.
# '''
# print(dedent(fill(sample_text, width=150)))

#30
# a=3.1426
# print(round(a,2), 'is answer')


##############  string ###############

#1
# import json
# json_obj ='{ "Name":"David", "Class":"I", "Age":6 }'
# python_obj = json.loads(json_obj)
# print("\nJSON data:")
# print(python_obj)
# print("\nName: ",json_obj["Name"])
# print("Class: ",python_obj["Class"])
# print("Age: ",python_obj["Age"])

#2
# import json
# # a Python object (dict):
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6
# }
# print(type(python_obj))
# # convert into JSON:
# j_data = json.dumps(python_obj)
#
# # result is a JSON string:
# print(j_data)

##############  list ###############

#6
# a=[(1,2),(4,5),(8,2),(1,3)]
# print(sorted(a,key = lambda x:x[-1]))

#7
# a=[(1,2),(4,5),(8,2),(1,3),(1,2)]
# b=[]
# duplicate=set()
# for i in a:
#     if i not in b:
#         b.append(i)
#         duplicate.add(i)
# print(b)
# print(duplicate)

#12
# a=[12,3,4,5,564]
# def delete(*x):
#    for k in x:
#        a.pop(k)
#    return a
# print(delete(2,0))

#13
# array=[[['*' for i in range(6)] for i in range(4)] for i in range(3)]
# print(array)

#15
# from random import shuffle
# a=[12,3,2]
# shuffle(a)
# print(a)

#21
# a=['d','e','erf']
# b=''.join(a)
# print(b)


#23
# from itertools import chain
# print (list(chain([1,2,3,4],['a','b','c','d'])))

# a=[[1,2,3,4],['a','b','c','d']]
# print(sum(a,[]))

#30
# from collections import Counter
# z=Counter(a)
# print(z)

#39
# a=[1,2,3]
# z=int(''.join(map(str,a)))
# print(z)

#44
# b=[]
# a=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
# j = 0
# for i in range(4):
#          b.append(a[j:j+5])
#          j=j+5
#
# print(b)


#45
# L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
# (7, 8), (9, 10)]
# s = []
# for i in L:
#     s.extend(i)
# print(s)

#47
# from itertools import chain
# elem1 = ['Red', 'Green', 'Black']
# elem2 = ['c', 'c', 'c']
#
# print(list(chain(*(zip(elem2, elem1)))))


#49
# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])


##############  dictionary ###############

#1
# a={1:2,12:3,3:4,4:5,0:5}
# a=dict(sorted(a.items(), key = lambda x:x[0]))
# print(a)


#2
# a.update({1:50})
# print(a)
# a[3]=40
# print(a)


#3
# dic1 = {'d': 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 ={**dic1 , **dic2 , **dic3}
# print(dic4)

#4
# if 50 in dic4:
#     print('present')
# else:
#     print('absent')


#5
# for i ,j in dic4.items():
#     print(i,'->',j)


#6
# dic=dict()
# n=int(input('any number.......'))
# for i in range(1,n+1):
#     dic[i]=i**3
# print(dic)

#10
#print(sum(dic4.values()))

#11
# dic = {3: 30, 4: 40, 2: 40, 5: 50, 6: 60}
# mul=1
# for i in dic:
#     mul=mul*dic[i]
# print(mul)

#12
# dic.pop(5)
# print(dic)

#15
# print(max(dic.values()))
# print(min(dic.values()))
# print(len(dic))

#19
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)
# print(Counter(d1))

##############  Tuple ###############

#1
# a=()
# print(a)

#3
# b=(1,2,34)
# # print(b)
# # print(b[1])

#4
# a,c,d=b
# print(a)
# print(a+c+d)

#5
# b=b+(4,45)
# v=b
# print(v)

#14
# #create a tuple
# tuplex = tuple("index tuple")
# print(tuplex)
# #get index of the first item whose value is passed as parameter
# index = tuplex.index("p")
# print(index)


#16
# tuple=((1,'f'),(2,'t'))
# dict=(dict((x,y) for x,y in tuple))
# print(dict)


##############  Set ###############

#1
# set={1,34,'e'}
# print(set)

#2
# set.add(21)
# print(set)
# set.update([80])
# print(set)

#4
# set.remove(80)
# print(set)


##############  Collection ###############

#1
from collections import Counter,deque
# a=Counter(a=100,b=100,w=40)
# e=(list(a.elements()))
# print(e)

#2
# m=Counter(e).most_common(1)
# print(m)


#3
# dq=deque(['weff','qerf'])
# for i in dq:
#     print(i)

#8
# import collections
# # Create a deque
# deque_colors = collections.deque(["Red","Green","White"])
# print(deque_colors)
# # Append to the left
# print("\nAdding to the left: ")
# deque_colors.appendleft("Pink")
# print(deque_colors)
# # Append to the right
# print("\nAdding to the right: ")
# deque_colors.append("Orange")
# print(deque_colors)
# # Remove from the right
# print("\nRemoving from the right: ")
# deque_colors.pop()
# print(deque_colors)
# # Remove from the left
# print("\nRemoving from the left: ")
# deque_colors.popleft()
# print(deque_colors)
# # Reverse the dequeue
# print("\nReversing the deque: ")
# deque_colors.reverse()
# print(deque_colors)

##############  Array ###############

#1
from array import *
# arr=array('i',[1,2,3,4,5])
# for i in arr:
#     print(i)
# print(arr)

#3
# arr.reverse()
# print(arr.itemsize)

#4
# arr1=array('u',['d','f','e','d'])
# print(arr1.itemsize)

#5
# print(arr1.buffer_info())


#6
# c=arr1.count('d')
# print(c)

#13
# list=arr1.tolist()
# print(list)


############## Python Conditional Statements and loops ##############

#4
# row=int(input('enter row.......'))
# for i in range(1,row+1):
#     print(i*'*')
# for i in range(row-1,0,-1):
#     print(i*'*')

#11
# from numpy import *
# r=int(input('enter row.......'))
# c=int(input('enter column......'))
# for i in range(r):
#     for j in range(c):
#         a=[[i*j for j in range(c)] for i in range(r)]
# print(a)

#14
# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)


#15
# from re import search
# p=input('password:  ')
# z=True
# while z:
#     if len(p)<6 :
#         break
#     elif not search('[a-z]',p):
#         break
#     elif not search ( "[0-9]" , p ) :
#         break
#     elif not search ( "[A-Z]" , p ) :
#         break
#     elif not search ( "[$#@]" , p ) :
#         break
#     else:
#          print('right password')
#          z=False
#          break
# if z:
#     print('wrong password')


############## Lambda ##############

#1
# a=lambda x:x+15
# print(a(10))

#6
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# print("\nSquare every number of the said list:")
# square_nums = list(map(lambda x: x ** 2, nums))
# print(square_nums)
# print("\nCube every number of the said list:")
# cube_nums = list(map(lambda x: x ** 3, nums))
# print(cube_nums)


############## class ##############

#1
# class myclass:
#     def myfunc(self,num):
#         if num==1:
#             return 'a'
#         if num==2:
#             return 'b'
#         if num==3:
#             return 'c'
#         if num==4:
#             return 'd'
#         if num==5:
#             return 'e'
# print(myclass().myfunc(5))

#3
# class parenthesis:
#     def valid(self,str):
#         for i in range(20):
#             a = [ ]
#             if '(' in str:
#                  i=str.index('(')
#                  if ')'in str[i:]:
#                        a.append('belal')
#                  else:
#                      a=[]
#                      break
#             if '{' in str:
#                  i=str.index('{')
#                  if '}'in str[i:]:
#                        a.append('belal')
#                  else:
#                      a=[]
#                      break
#             if '[' in str:
#                 i=str.index('[')
#                 if ']'in str[i:]:
#                        a.append('belal')
#                 else :
#                     a = [ ]
#                     break
#         if len(a)>0:
#             print('valid')
#         else:
#             print('invalid')
# # parenthesis().valid('[]{}()')
# # parenthesis().valid('[]{()')
# parenthesis().valid(']{}()')
# parenthesis().valid('()()()()()()()()()(()')

#9
# class IOString():
#     def __init__(self):
#         self.str = ""
#
#     def get_String(self):
#         self.str = input()
#
#     def print_String(self):
#         print(self.str.upper())
#     def reverse(self):
#         print(list(reversed(self.str.split(' '))))
#
# str1 = IOString()
# str1.get_String()
# str1.print_String()
# str1.reverse()
#
# str2 = IOString()
# str2.get_String()
# str2.print_String()

#10
# class Rectangle:
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def result(self):
#         return self.length*self.width
# r1=Rectangle(12,10)
# print(r1.result())

############## Tkinter ##############

#1
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter.ttk import Progressbar

def showtext():
    print('this is a simple text')

parent=Tk()
parent.title('welcome to python')

#--------------------form
# name = Label(parent, text = "Name").place(x = 30, y = 50)
# email =Label(parent, text = "User ID").place(x = 30, y = 90)
# password = Label(parent, text = "Password").place(x = 30, y = 130)
# sbmitbtn =Button(parent, text = "Submit", activebackground = "green", activeforeground = "blue").place(x = 120, y = 170)
# entry1 = Entry(parent).place(x = 85, y = 50)
# entry2 = Entry(parent).place(x = 85, y = 90)
# entry3 =Entry(parent).place(x = 90, y = 130)

#-----------------frame
# frame=Frame(parent)
# frame.pack()

#-----------------widget
# mylavel=Label(parent,text='Enter input', font=('Arial Bold', 80))
# mylavel.pack()
#mylavel.grid(column=0, row=0)

#------------------spinbox
spin_box = Spinbox(
    parent,
    from_=0.6,
    to=50.0,
    increment=.01,
    textvariable=DoubleVar()
)
spin_box.pack()

#--------------------button
# textdisp=Button(frame,text='hello',command=showtext)
# textdisp.pack(side=LEFT)
# my_button = Button(frame, text='Quit',fg='green', height=1, width=5, command=parent.destroy)
# my_button.pack(side=RIGHT)

#-------------------checkbox
my_checkbutton = Checkbutton(
    text="Check when the option True",
    variable=BooleanVar()
)
my_checkbutton.pack()

#-------------------combobox
my_combobox = ttk.Combobox(
    parent, textvariable = StringVar(),
    values=["PHP", "Java", "Python"])
my_combobox.pack()

#-----------------radiobutton
radio1 = Radiobutton(parent, text='First', value=1)
radio2 = Radiobutton(parent, text='Second', value=2)
radio3 = Radiobutton(parent, text='Third', value=3)
radio1.pack()
radio2.pack()

#------------------scrolltext
txt =tkst.ScrolledText(parent, width=40, height=10)
txt.pack()

#------------progressbar
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(parent, length=220, style='black.Horizontal.TProgressbar')
bar['value'] = 80
bar.pack()

#---------------listbox
label1 = Label(parent,text = "A list of favourite languages...")
listbox = Listbox(parent)
listbox.insert(1,"PHP")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")
label1.pack()
listbox.pack()

parent.geometry("800x500")
parent.mainloop()