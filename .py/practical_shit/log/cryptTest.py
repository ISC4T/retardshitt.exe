from cryptography.fernet import Fernet
 
# we will be encryting the below string.
message = ((("Username" + "\n") + "Password") + "\n")
 
# generate a key for encryptio and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key
 
#key = LFwKurPGqvtJ5pj0HYnV224ZJkKWcA4m
 
# Instance the Fernet class with the key
 
f = Fernet(b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=')
 
# then use the Fernet class instance
# to encrypt the string string must must
# be encoded to byte string before encryption
encMessage = f.encrypt(message.encode())
 
print("original: ", message)
print("encrypted: ", encMessage)
 
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = f.decrypt(encMessage).decode()
 
print("decrypted: ", decMessage)