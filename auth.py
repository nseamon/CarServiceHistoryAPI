import binascii
import hashlib
import os


def generateSaltAndHash(password):
    """
    Generates a salted and hashed password

    :return: a tuple object (<salt>, <hashed_pw>)
    """
    salt = hashlib.sha256(os.urandom(16)).hexdigest().encode('ascii')
    hashed_pw = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100)
    hashed_pw = binascii.hexlify(hashed_pw)
    return (salt.decode('ascii'), hashed_pw.decode('ascii'))


def validatePassword(password, salt, stored_pw):   
    """
    Validates input plaintext password against stored password/salt

    :returns: boolean for password validity
    """

    new_hashed_pw = hashlib.pbkdf2_hmac('sha512', password.encode('ascii'), salt.encode('ascii'), 100)
    
    if stored_pw == binascii.hexlify(new_hashed_pw).decode('ascii'):
        return True
    
    return False
