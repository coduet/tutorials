
# function are declared/defined using "def" keyword
# code inside a function is idented
def print_hello(name):
    print("hello " + name)

def check_valid_age(age):
    print("Checking if you age is valid")
    print(".........")
    if(age >= 18) :
        return True
    else : 
        return False


name = input("Enter your name : ")
print_hello(name)

age = int(input("Enter your age : "))
if(check_valid_age(age)) :
    print("Siuuuuuu!! Your age is valid")
else : 
    print("Go home kid")