import hashlib

def MD5(str):
    str=str.encode()
    md5_hash = hashlib.md5(str)

    print("MD5 Hash:", md5_hash.hexdigest())

def SHA(str):
    str=str.encode()
    sha_hash = hashlib.sha1(str)
    print("SHA Hash:",sha_hash.hexdigest())
    
str=input()
MD5(str)
SHA(str)
    