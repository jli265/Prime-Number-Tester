# find out prime numbers between 1 and the number you enter.
import math
try:
    N=int(input("Enter the biggest positive integer(N>1) that you would test:"))
except:
    print("Error! Please enter an integer greater than 1! Try again!")
    exit()
is_prime=True
prime_list=[]
prime_list.append(2)
prime_list.append(3)

if N <=1:
    print("Error! Please enter an integer greater than 1! Try again!")
elif N==2:
   print("Prime number is 2.")
   print("There is 1 prime number between 1 and 2.")
elif N==3:
   print("Prime numbers are 2, 3.")
   print("There are 2 prime numbers between 1 and 3.")
else:
  m=4
  count = 2
  for n in range(m,N+1):
    if n % 2 == 0 :
        continue
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n % i ==0:
            is_prime=False
            break
    if is_prime==True:
            count+=1
            prime_list.append(n)
    else:
        is_prime=True
  print("Prime numbers are shown below in a list.")
  print(prime_list)
  print("There are %d prime numbers between 1 and %d."%(count,N))






