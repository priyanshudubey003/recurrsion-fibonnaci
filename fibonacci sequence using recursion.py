def fib_rec(x):
    if x <=1:
        return x
    else:
        return(fib_rec(x-1)+fib_rec(x-2))
# Take input for number of terms from user
num_terms=int(input("How many terms? "))
for i in range(num_terms):
 print(fib_rec(i))
