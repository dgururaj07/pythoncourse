#pythons supprots 2 types of functions
    #- Built in & user defined

# - function
#   every funtion should start with the def keyword 
#       and mention the function name
#       returns empty or values
#       access modifier is public by default


#function:
def   getvalue(data): {
print(data)
}

getvalue("feeed")

def add_num():
    a=10
    b=20
    print(a+b)
add_num()  

def addNum():
    a,b = 100,200
    print(a+b)

addNum()  


#Types of arguments:
#-required or position argument
# - keyword argument
#-default argument
#-variable length argument


def addnumwith_args(a,b):
    a+b

print(addnumwith_args(10,40))




def addnumwithmanyargs(a,b,c=1):
    print(a,b,c)

addnumwithmanyargs(11,3)



def addItems(*args):
    print(args)
    print(type(args))
    print(sum(args))


addItems(1,2,3,4,5) 

def printDict(**kwargs):
    print(kwargs)
    print(type(kwargs))
    


printDict(a=1,b=2,c=3)



def collectionofdata(a,*args,**kwargs):
    print(a,args,kwargs)



collectionofdata(1,2,3,4,5,6,x=10,y=12,z=14)   






