import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#Prime number
p=int(input("Enter the prime number :"))
isPrime(p)
#primitive root (G)
G=int(input("Enter the primitive root:"))

'''def is_primitive(n):
    phi=p-1
    bool flag=True
    for g in range(2,p):
        for i in range(1,phi):
            g=pow(p,i)
            if(g==1):
                False
                break
            else:
                True
                
    if(flag == True):
        
            
'''

#private key of A

Ai=int(input("Enter the private key for A:"))
if(Ai < p):
    Ap = Ai 
else:
    print("Enter the value of private key less than Prime number")

#private key of B
Bi=int(input("Enter the private key for B:"))
if(Bi < p):
    Bp=Bi
else:
    print("Enter the value of private key less than Prime number")
    

#public key for A 
x=int(pow(G,Ap,p))
print("Public key of A is :",x)

#public key for B
y=int(pow(G,Bp,p))
print("Public key for B is :",y)

#Secret key for A
ka=int(pow(y,Ap,p))
print("Secret key of A is :",ka)

#secret key for B
kb=int(pow(x,Bp,p))
print("Secret Key For B is:",kb)



