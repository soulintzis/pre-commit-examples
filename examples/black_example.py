# """The following example demonstrate how we can use Black to better format our code"""
# def calculate_factorial(number):
#   """A function with wrong indentation (2 spaces instead of 4)"""
#   if number == 0:
#     return 1
#   else:
#     return (
#       number * calculate_factorial(number - 1)
#     )

# """That should have been in one line of code"""
# num = int(
#     input(
#         "Enter a number: "
#         )
#     )

# """The operator should had been surrounded with spaces"""
# if num<0:
#     print("Invalid input")


# """A function with a lot of arguments that should be on seperate lines of code"""
# def a_function_with_a_lot_of_arguments( name, default=None,*args,variable = "1123",a='1', b = '2',c , another_variavle='value' ,an_array,test,ad,office,d,e,f,**kwargs):
#   pass

# """Wrong formated list of numbers"""
# j = [1,
#  2, 3
# ]

# def function_1():
#   """Functions outside a class should be seperated by two lines"""
#   pass
# def function_2():
#   """Also variables outside a class should be seperated by two lines"""
#   pass
# names = ['John', 'George']

# class RandomClass:
#   names = ['John', 'George']
#   def function_1(self):
#     """Functions inside a class should be seperated by one line"""
#     pass
#   def function_2(self):
#     """Also variables inside a class should be seperated by one line"""
#     pass
