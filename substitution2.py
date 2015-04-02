'''
plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
ciphertext: XCPJLAKEBOMTWYSUDQNGRZFHIV

Would have translation table:

table={'A':'X', 'B':'C', 'C':'P'... 'Y':'I','Z','V'}
'''

'''
This function generates a random translation table
for all 128 ASCII characters and returns it.
'''
import random 
def generate_table():
    asciilist=[]
    for i in range(0,128):
        asciilist+=(chr(i))
    listcopy = asciilist[:]
    random.shuffle(listcopy)
    gentable=dict(zip(asciilist, listcopy))
    return gentable
 


'''
This function takes a translation table (dictionary) as an argument and
produces a new, reversed table. Each key-value pair is swapped;
the key becomes the values and the value becomes the key. A new
dictionary storing the reversed table is returned.

If the initial translation table represented:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
XCPJLAKEBOMTWYSUDQNGRZFHIV

The resulting translation table would represent:
XCPJLAKEBOMTWYSUDQNGRZFHIV
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''
def reverse_table(table):
    reverse_output_table={v:k for k, v in table.items()}
    return reverse_output_table

'''
This function takes a string as input and produces a dictionary containing
a translation table. The character at the ith position in the string is the
result of translating character i. In our running example,

plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
ciphertext: XCPJLAKEBOMTWYSUDQNGRZFHIV

The input string would be:
"XCPJLAKEBOMTWYSUDQNGRZFHIV"

The resulting dictionary corresponding to the translation table
is returned.
'''

def string_to_table(table_string):
    string_list=list(table_string.strip())
    ascii_list2=[]
    for i in range(0,128):
        ascii_list2+=(chr(i))
    output_table=dict(zip(ascii_list2, string_list))
    return output_table
    

'''
This function takes a dictionary representing a translation table as
its input and produces a string representation of the translation table.
The character at the ith position in the string is table[i]. In our running
example, the output string would be:

"XCPJLAKEBOMTWYSUDQNGRZFHIV"

The resulting string representation is returned.
'''
def table_to_string(table):
    output_string=""
    for i in range(0,len(table)):
        output_string+=table[chr(i)]
    return output_string

'''
This function takes two arguments, a dictionary containing a
translation table and a plaintext string we would like to encrypt.
Using the translation table, it encrypts the string and returns the
ciphertext.
'''
def encrypt(table,string):
    encrypted=""
    for a in string:
        encrypted+=table[a]
    return encrypted

'''
This function takes two arguments, a dictionary containing a
translation table and an encrypted string we would like to decrypt.
It reverses the translation table and decrypts the string. It returns the
resulting plaintext.
'''
def decrypt(table,string):
    decrypted=""
    new_table=reverse_table(table)
    for a in string:
        decrypted+=new_table[a]
    return decrypted


'''
This function takes a single string argument. It opens the file with the
name in the parameter string_name and reads in a single string
representation of a translation table. It converts this string into
a table (calling the string_to_table function.) It returns the resulting
table.
'''
def read_table(file_name):
    f=open(file_name,'rb')
    t=f.read()
    output=string_to_table(t)
    return output

'''
This function takes two arguments: table, which is a dictionary
representing a translation table and file_name, which is a string
holding the name of a file. This function opens a file named file_name
and writes a string representation of table into that file.
'''
def write_table(table,file_name):
    s=table_to_string(table)
    f=open(file_name, 'wb')
    f.write(s)
    f.close()
    return 

'''
This function reads the plaintext in in_file, encrypts it using the
key in table_file, and writes the resulting ciphertext in out_file.
'''
def encrypt_file(in_file,out_file,table_file):
    f=open(in_file, 'rb')
    t=f.read()
    g=open(table_file, 'rb')
    h=g.read()
    a=string_to_table(h)
    x=encrypt(a,t)
    b=open(out_file, 'wb')
    b.write(x)
    b.close()
    return

'''
This function reads the ciphertext in in_file, decrypts it using the
key in table_file, and writes the resulting plaintext in out_file.
'''
def decrypt_file(in_file,out_file,table_file):
    f=open(in_file, 'rb')
    t=f.read()
    g=open(table_file, 'rb')
    h=g.read()
    a=string_to_table(h)
    x=decrypt(a,t)
    b=open(out_file, 'wb')
    b.write(x)
    b.close()
    return


decrypt_file("substitution.enc","substitution.txt","substitution.key")
