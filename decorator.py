def decorator(func):
    def inner():
        print("before the function is called")
        func()
        print("after the function is called")
    return inner

@decorator
@decorator
def my_function():
    print("This is inside the function")

my_function()

def add_two(func):
    def inner(x,y):
        return func(x,y)+2
    return inner

@add_two
def my_function(x,y):
    return x+y


print(my_function(1,2))







# Function to be decorated should give me the first name of a person
# Its decorator should return the first name as a string with is awesome attached if the name starts with a [k ,s ,a d]
# if not not it should says that the name smells like teen spirit
# There needs to be also some driver code

names=['Jody S', 'Jacoby Y', 'Alex C', 'Dylan K', 'Kevin B', 'Andre L', 'Dmitry U', 'Francisco G', 'Sarah S', 'Gio M', 'Shayne H']

def add_suffix(func):
    def inner(s):
        if func(s)[0].lower() in ['k','s','a','d']:
            return func(s) + " is awesome"
        else:
            return func(s) + " smells like Teen Spirit"
    return inner

@add_suffix
def first_name(s):
    first = s.split()[0]
    return first

for name in names:
    print(first_name(name))


