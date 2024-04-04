# Errors and Exceptions

a = 5
#print(a))  , this is an example of a syntactical error

#Exception error
#Ex: trying to add an integer to the string
# a = 5 + '10'

#file not found

#f = open('somefile.txt')

# x = -5
# if x < 0:
#     raise Exception('x should be positive')

#x=-5
#assert (x>=0) , 'x is not positive'  # if not true it will raise exception

#handle exception

# try:
#     a = 5 / 0
#     b = 1 + "try"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
#else:
#     print("everything is fine")
#finally:
#     print("cleaning up....")


#define our own exceptions

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError('Value is too small')
    
try:
    test_value(4)
except ValueTooHighError as e:
    print(e);
except ValueTooSmallError as e:
    print(e)

