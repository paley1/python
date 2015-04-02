user_input=raw_input("type a word:")
x=len(user_input)-1
y=""
while x >=0:
    cur_char=user_input[x]
    y=y+cur_char
    x=x-1
if y==user_input:
    print user_input +", " + "Congrats, this is a palindrome!"
else:
    print user_input +", " + "This is not a palindrome!"
