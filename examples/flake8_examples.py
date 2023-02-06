"""This file demostrates example of flake8 configuration"""

# numbers = [1, 2, 3]
"""bugbear: variable x doesn't used within the loop body"""
# for x in numbers:
#     print(1)

"""The use of bare `except` is considered bad practice, because it catches unexpected events"""
# try:
#     print('success')
# except:
#     print('error')

"""Do not call assert False since python -O removes these calls"""
# assert False
# assert False, "message"


# class Warnings:
# def __init__(i_am_special):
#     """First argument should be `self`"""
#     pass

# def almost_a_class_method(cls, arg1):
#     """First argument should be `self`, or should be defined as class method"""
#     pass

# def almost_a_static_method():
#     """First argument should be `self`, or should be defined as static method"""
#     pass

# @classmethod
# def wat(self, i_like_confusing_people):
#     """First argument should be `cls`, or should not be defined as class method"""
#     pass

# def i_am_strange(*args, **kwargs):
#     """First argument should be `self`"""
#     args[0]


#     def defaults_anyone(self=None):
#         ...

#     def invalid_kwargs_only(**kwargs):
#         ...

#     def invalid_keyword_only(*, self):
#         ...

#     async def async_invalid_keyword_only(*, self):
#         ...

"""Pointless comparisons"""
# 1 == 1
# 1 in (1, 2)


# def test():
#     """Pointless comparison"""
#     1 in (1, 2)


foo = [1, 2]


def f(x):
    return x


# """Unnecessary generators"""
# list(f(x) for x in foo)
# """Writen as list comprehension"""
# [f(x) for x in foo]

# """Unnecessary generators"""
# set(f(x) for x in foo)
# """Writen as set comprehension"""
# {f(x) for x in foo}

# """Unnecessary generators"""
# dict((x, f(x)) for x in foo)
# """Writen as dict comprehension"""
# {x: f(x) for x in foo}

# """Unnecessary generators"""
# set([f(x) for x in foo])
# """Writen as set comprehension"""
# {f(x) for x in foo}

# """Unnecessary generators"""
# dict([(x, f(x)) for x in foo])
# """Writen as dict comprehension"""
# {x: f(x) for x in foo}

"""unnecessary list passed to tuple()"""
tuple([1, 2])
"""Writen as tuple"""
(1, 2)

"""unnecessary list passed to tuple()"""
tuple([])
"""Writen as tuple"""
()

# list([1, 2])
# #  [1, 2]

# list([])
# #  []

# set((1, 2))
# #  {1, 2}

# set([])
# #  set()

# dict([(1, 2)])
# #  {1: 2}

# dict([])
# #  {}

# list([f(x) for x in foo])
# #  [f(x) for x in foo]


# class pep8_naming:
#     """Class name 'pep8_naming' should use CapWords convention"""

#     def SUM(self, a, B):
#         """Function name 'SUM' should be lowercase"""
#         """Argument name 'B' should be lowercase"""
#         """Variable 'AplusB' in function should be lowercase"""
#         AplusB = a + B
#         return AplusB
