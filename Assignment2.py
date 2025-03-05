import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("---- Let's encrypt and decrypt the message using RSA -----")
while True:
    p = int(input("Enter a prime number P: "))
    q = int(input("Enter a prime number Q: "))
    if isPrime(p) and isPrime(q):
        break
    else:
        print("Both numbers must be prime. Please enter again.")


n = p * q
#print("value of n:{n}")
phi = (p - 1) * (q - 1)
#print("value of phi_of_n is:{phi}")

#e is public key
for e in range(2, phi):
    if math.gcd(e, phi) == 1:
        break


#d is the private key
for d in range(2, phi):
    if (d * e) % phi == 1:
        break


print(f"\nPublic key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")


m = int(input("\nEnter message as a number: "))

#  For Cipher text
ct = (m**e) % n 
print(f"\nEncrypted message: {ct}")

# for Decryption of msg
dt = (ct**d) % n
print(f"Decrypted message: {dt}")

