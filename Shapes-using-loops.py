# For triangle Shape 
number= int(input("entre your number : "))
for x in range(1,number+1):
    print(" "* (number-x),end=" ")
    print(" * "* (2*x-1),end=" ")
    print("")

# For Box Shape 
number= int(input("entre your number : "))
for x in range(1,number+1):
    if(x==1 or x==number):
        print("*"*number)
    else:
        print("*", end="")
        print(" "*(number-2),end="")
        print("*", end="")
        print("")







