# # def even_number():
# #     i =1 
# #     while  i< 50:
# #         i+=1
# #         if i%2==0:
# #          continue 
# #         print(i)
# # even_number()

# # def even(name):
# #     n= [0]
# #     char_even=name[n%2==0]
# #     return char_even
# # even("Linda")

# # def display_even():
# #     text=str(input("Please enter your string:"))
# #     for name in text:  
# #          x=name[::2]
# #          print(x) 

# def even_indices():
#     x= str(input("Enter a word: "))
#     for i in range(len(x)):
#         if i%2==0:
#           print(x[i])
# # even_indices()     

# def multipl_table():
#     i=1
#     while i<=10:
#         produit = i*10
#         print(f"{i} x 10 is {produit}")
#         i+=1
# # multipl_table()

# def loop_sum():
#     prev_number=0
#     for i in range (1,11):
#         sum = prev_number+i
#         print(f"Previous number: {prev_number}, current number: {i}, sum: {sum}")
#         prev_number =i
# loop_sum()

# def string_slicing(str,n):
#     print (str[4:n])
# # string_slicing("antananarivo",12)  

# # def lists():
#     list = [1,2,3,4,5,1]
#     if list[0]==list[-1]:
#         # print(True)
#     # else:
#         # print(False)
# # lists()  


# # def divisible_by_five():
#     # x=[10,20,33,46,55]
#     # for n in x:
#     #     if n%5==0:
#     #         print(n)
# # divisible_by_five()

# # def sub_string():
# #     word = "Emma is a good developer. Emma is a writer"
# #     z=word.count("Emma")
# #     print(f"Emma appears {z} times")
# # sub_string()    

# for num in range(10):
#     for i in range(num):
#         print (num, end=" ")
#     # print("\n")

# def palindrome(int):
#     num1=int
#     num2=reversed(num1)
#     if num1==num2:
#         print("The number is palindrome")
#     else:
#         print("The number is not palindrome")    
# palindrome(125)     

# from ntpath import join
# from unicodedata import name


# def comprehension():
#     x = [100,110,120,130,140,150]
#     y = [n*5 for n in x]   
#     print(y)
# comprehension()

# def divisible_by_three(n):
#     for num in range(1,n):
#         if num%3==0:
#             print(f"{num} is divisible by 3")
# divisible_by_three(20)     

# def flatten_list():
#     x = [[1,2],[3,4],[5,6]]
#     y = []
#     for n in x:
#         for m in n:
#             y.append(m)
#     print(y)        
# flatten_list()

# def smallest(l):
#     l.sort()
#     print(l[0])
# smallest([5,4,3,8,9,7,6,1,4])   

# def remove_duplicates():
#     x = ['a','b','a','e','d','b','c','e','f','g','h']
#     y = set(x)
#     print(y)
# remove_duplicates()    

# def divisible_by_seven():
#     div_by_seven = []
#     for n in range(100,201):
#         if n%7==0:
#             div_by_seven.append(n)
#     print(div_by_seven)
#     return div_by_seven
# divisible_by_seven()            

# def greet_student():
#     students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
#     i = 0
#     while i < len(students):
#         year = 2022 - students[i]["age"]
#         name = students[i]["name"]
#         # print(f"Hello {name}, you were born in the year {year}")
#         print(len(students))
#     i+=0    
# greet_student()   

      
