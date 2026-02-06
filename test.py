# Write a function to find maximum of three number in python.
# def maximum_num(a,b,c):
#     if a > b and a > c:
#         print(a,"is gretest value")
#     elif b > c:
#         print(b,"is gretest value")
#     else:
#         print(c,"is gretest value")
# maximum_num(5,7,9)


# Write a function to create and print a list where the values are square of number between 1 and 30.
# def create_list():
#     l = []
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(create_list())


# Write a function that takes a number as a parameter and check if the number is prime
# def check_prime_num(n):
#     if n == 1:
#         print(n,"its not prime number")
#     for i in range(2,n):
#         if n % i == 0:
#             print(n,"number is not prime")
#             break
#     else:
#         print(n,"number is prime")
# check_prime_num(37)


# Write a function to sume all the numbers in list
# def add(list):
#     total = 0
#     for i in list:
#         total += i
#     return total
# print(add([1,2,3,4,5]))

# Solution 2
# def add(list):
#     if len(list) == 1:
#         return(list[0])
#     else:
#         return((list[0]) + (add(list[1:])))

# print(add([1,2,3,4,5,6]))

# Write a function to solve the fibonacci sequence using recursion.
# def fs(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return (fs(num-1) + fs(num-2))
# print(fs(21))