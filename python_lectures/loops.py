# for i  in range (0,7):
#     print(i) 
# ----------------------------------
# l = [1, 7, 8]
# for items in l:
#     print(items)
# else:
#     print("done")
# ---------------------------------
# for i in range(0,80):
#     print(i)
#     if  i == 3:
#       break
# ------------------------------
# for i in range (0,10):
    
#     if i == 1:  
#        continue
#     print(i)
# ------------------------------
# i = 0 
# while i<10:
#         print("the value of i :",i)
     
#         if (i==3):
#          print("-------X--------",i)
#         i += 1
# else:
#     print("continuous....",i)

        
        
#list1 = [3, 43, 2, False, 6.3,"prashant"]
# # index = 0 
# # for item in list1:
# #     print(item, index)
# #     index += 1
# for index, item in enumerate(list1):
#     print(index,item)
    
# for i, letter in enumerate('abcde'):
#     print('index is {}and value is {}'.format(i,letter))


    
# ------------------------------
# pass is a null statement
# list ={'k1':'fruits','bike':'bullet','car':'tata'}
# for k, v in list.items():
#     print(k)
#     print(v)

# -------------------------------------  
# list1 = list(range (0,51))
# print(list1)
# ---------------------------------------
# dict = {'key':'chavi', 'fruits':'mango','road':'rasta'}
# for index, item in enumerate(dict):
#     print(index,item)
# ----------------------------------------
# names = ("prashant","akshay","shreyash")
# if "akshay" in names:
#     print("akshay found")

num = [1, 2, 3,4,5]
print(max(num))
print(min(num))
new = [i+2 for i in num]
print(new)

l1 = [ z for z in range (11) if z%2==0]
print(l1)

