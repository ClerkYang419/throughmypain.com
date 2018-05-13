import sys

sys.setrecursionlimit(1000) #expend the limit recursion number of python

FibS = [0,1]    # initial list already has two digits

#recursion to add digit into the list
def Fib(i,a,b):
    c = a+b
    FibS.append(c)
    if i < 1000:
        i = i+1
        return Fib(i,b,c)
    else:
        return FibS

a = Fib(3,0,1)
#print(a)        #Entire 1000+ number digits
print(a[999])   #the 1000th digit

