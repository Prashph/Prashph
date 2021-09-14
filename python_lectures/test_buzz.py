# n=int(input("enter a number"))
# for i in range(n):
#     if i%3==0 and i%5==0:
#         print("Fizzbuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:                          -->>for loop
#         print("Buzz")
#     else:
#         print(i)

#-------------------------------
# class Solution(object):

#     def fizzBuzz(self,n):
#         '''
#         :type n:int
#         rtype:List[str]
#         '''
#         result = []
#         for i in range(1,n+1):     
#             if i%3==0 and i%5==0:
#              result.append("Fizzbuzz")
#             elif i%3==0:
#                 result.append("Fizz")
#             elif i%5==0:                          #-->>for loop
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))
#         return result
# obj = Solution()
# print(obj.fizzBuzz(17))
#------------------------------->
# def fizzBuzz(n):
#     for x in range(n):
#         if x%3==0 and x%5==0:
#             print("fizzbuzz")
#         elif x%3==0:
#             print("fizz")
#         elif x%5==0:
#             print("buzz")
#         else:
#             print(x)
# n=int(input("enter a number"))
# print(fizzBuzz(n))


