'''
This function takes a string representing the key and an integer i representing a "nonce". It uses the sha-256
cryptographic hash algorithm to return a hash value between 0 and 128.
This will be used to produce a key stream.
'''
import hashlib
def nonce_hash(key,i):
    return int(hashlib.sha256(key+str(i)).hexdigest(),16)%128

'''
This function takes a string representing a key, an index i representing
the position in the stream, and a character c. The function should use the
index and the key as a nonce to produce the next value in the key stream
(by calling nonce_hash) and xor this with the ASCII code for c (use the ord
function.) This will produce a result between 0 and 128. Convert that
back to a character (using the chr function) and return the result.
'''
def enc_char(key,i,c):
    a=nonce_hash(key,i)
    output=(chr(a^(ord(c))))
    return output

'''
This function takes a string representing a key and a string s. It should
iterate over the string one character at a time, encrypting them using
the stream cipher (calling enc_char). The resulting encrypted string
should be returned.
'''
def enc_str(key,s):
    x=len(s)
    n=0
    encrypted_string=""
    while n<x:
        c=s[n]
        e=enc_char(key,n,c)
        encrypted_string+=e
        n+=1
    return encrypted_string

'''
This function reads the ciphertext in in_file, decrypts it using the
key in key_file, and writes the resulting plaintext in out_file.
'''

def encrypt_file(in_file,out_file,key_file):
    f=open(in_file, 'rb')
    t=f.read()
    g=open(key_file, 'rb')
    h=g.read()
    x=enc_str(t,h)
    b=open(out_file, 'wb')
    b.write(x)
    b.close()
    return

encrypt_file("stream.enc","stream.txt","stream.key")
