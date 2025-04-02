from Crypto.Cipher import AES 
from secrets import token_bytes

key=token_bytes(16)
cipher=AES.new(key,AES.MODE_EAX)
nonce=cipher.nonce
msg=input("Enter Msg:")
msg=msg.encode()
ciphertext=cipher.encrypt(msg)
print("Ciphertext is:",ciphertext)


cipher=AES.new(key,AES.MODE_EAX,nonce=nonce)
plaintext=cipher.decrypt(ciphertext)
print("Plaintext is:",plaintext)





















































