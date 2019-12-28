import hashlib
import os

def generateSaltAndHash(password):
    salt = os.urandom(32)
    hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    return (salt, hashed_pw)

def validatePassword(password, salt, hashed_pw):   
    new_hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    if hashed_pw == new_hashed_pw:
        return True
    else: 
        return False
