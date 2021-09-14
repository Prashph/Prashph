# def rectangle(m,n):
#     for i in range(m):
#         print('#'*n)
# rectangle(2,4)
# def rectangle(m,n):
#     print("#"*m)
#     print("#"*n)
# rectangle(4,4)

#--------------------
#2------------------
# def add_excitment(string,n):
#     print(string,n)
# string=input("enter your name: ")
# print(add_excitment(string,'!'))
# a="prash"
# print(a,"!")

#---------------------------
# def sum_digit(n):
#     print(sum(int(n) for n in str(n)))
# sum_digit(560)

#========================
# def binom(n,k):
#     return(int(n)/int(k*(n-k)))
# print(binom(2,4))

#--------------------------
# def number(n):
#     a=10**int(n-1)
#     b=10**int(n)-1
#     from random import randint
#     sol=randint(int(a),int(b))
#     print(sol)
# number(100)

#---------------
# def number_of_factor(n):
#     for i in range(1,n):
#         if n%i==0:
#             print("the factors are:",i)
# number_of_factor(6)
#---------------------------
# def number_of_factors(n):
#     list=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             list.append(i)
#     return list
# print(number_of_factors(6))
#-----------------------------
# def numbers(n):
#     L=[1,3,5,6,10]
#     x=[b for b in L if n>b]
#     largest=0
#     for num in x:
#         if num==x:
#             x==num
#     print(num)
# numbers(3)

#----------------------------
# def diff_position(string1,string2):
#     a=string1.replace(' ','')
#     b=string2.replace(' ','')
#     if len(a)>len(b):
#         length=len(a)
#     else:
#         length=len(b)
#     count=0
#     for i in range(length):
#         if  (str(a[i]!=b[i])):
#             count=count+1
#     print(length-count)
# diff_position('python','pzth')


#----------------------------
# def find_all(n):
#     x="hi my name is prashant and i learning python now"
#     y=x.count(n)
#     z=list(x)
#     for i in range (y):
#         a=z.index(n)
#         z.remove(n)
#         print(a+(i))
        
# find_all('a')
#-----------------------
# def change_case(n):
#     y=n.swapcase()
#     print(y)
# change_case('pRASHANT')
#-----------------------
# def is_sorted(n):
#     y=list(n)
#     if y==sorted(n):
#         print("True")
#     else:
#         print("False")
# is_sorted('python')
# is_sorted("app")
#-------------------------
# def one_away(x,n=2):
#     return (int(x)**(1/n))
# print(one_away(9))
#-----------------------
# def one_away(string1,string2):
#     count=0
#     for i in range(len(string1)):
#         if string1[i]!=string2[i]:
#             count+=1
#     if count==1:
#         print("true")
#     else:
#         print("false")
# one_away('hike','bike')
# one_away('prashant','prashant')
#----------------------------
# def prime(num):
#     count=0
#     for i in range(2,num):
#         if num%i==0:
#             count=count+1
#     if count>1:
#         print("not prime")
#     else:
#         print("prime")
        
# prime(45)
# prime(13)
# a=20/10*10

# print(a)


            








