from Crypto.Cipher import DES
from secrets import token_bytes

key=token_bytes(8)

cipher=DES.new(key,DES.MODE_EAX)
nonce=cipher.nonce
msg=input("Enter Msg:")
msg=msg.encode()

ciphertext=cipher.encrypt(msg)
print("Ciphertext is:",ciphertext)

cipher=DES.new(key,DES.MODE_EAX, nonce=nonce)
plaintext=cipher.decrypt(ciphertext)
print("Plaintext is:",plaintext)