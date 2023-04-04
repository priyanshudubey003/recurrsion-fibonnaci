#Fibonacci Series
n=int(input("Enter the number: ")) #Input from the user
c=0 #Assigning the value to c
a=1 #Assigning the value to a
b=1 #Assigning the value to b
if n==0 or n==1:       #Check for expceptions and special case
    print("Valid") 

else: #Else condition
    while c<n: #While condition
        c=a+b
        b=a
        a=c
    if c==n:
      print("Valid")
    else:
      print("Invalid") #While condition 
