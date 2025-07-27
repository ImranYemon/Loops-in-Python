number= int(input("entre your number : "))

for x in range(2,number):
    if (number%2)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime") 