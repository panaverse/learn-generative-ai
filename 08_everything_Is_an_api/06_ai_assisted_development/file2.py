# create function which takes two arguments as numbers and return sum als add type hints

def add(a,b):
    c=a+b
    return c

#create login function which takes username and password
def login(username,password):
    if username=="admin" and password=="admin":
        return True
    else:
        return False
    
def add_three_numbers(a,b,c):
    d = a+b+c
    return d