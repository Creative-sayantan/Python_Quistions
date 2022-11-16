#WAP to calculate GCD of two numbers.
a=int(input("enter first num : "))
b=int (input("enter the second num : ")) 
for i in range(1,a+1): 
  j=i  
  if a%i==0 and b%j==0:
    c=i
    print("The GCD of two num is",c)