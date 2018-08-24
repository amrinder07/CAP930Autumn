#Functions:

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True

n=input("enter number:")
for x in range(2,int(n)):
    if isprime(x):
        print(x,'is prime')
    else:
        print(x,'is not prime')
