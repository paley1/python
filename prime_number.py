user_input=int(raw_input("Please input a number"))
x=(1, user_input)
for i in range(1,user_input):
    if(i not in x):
        if user_input%(i) !=0:
            print "your input is prime"
        else:
            print "your input is not prime"
