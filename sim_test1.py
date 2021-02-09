test1 = "this is test"
print("test1")

def fibonacci_numbers_at_index(count):
    if count <= 1:
        return count
    else:
        return fibonacci_numbers_at_index(count - 1) + fibonacci_numbers_at_index(count - 2)
count = 5
i = 1
while i <= count:
    print(fibonacci_numbers_at_index(i))
    i += 1

def foo():
    pass
 
 
print(type(foo))

class Data:
    def foo(self):
        print('foo method')
 
 
def foo():
    print('foo function')
 
 
# calling a function
foo()
 
# calling a method
d = Data()
d.foo()
 
# checking data types
print(type(foo))
print(type(d.foo))

