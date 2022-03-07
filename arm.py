# whether the given number is ARMSTRONG number or not?
n=int(input('n:'))
temp=n
sum=0 #intialization the sum
#the sum of the cube of its digits
while temp>0:
  d=temp%10
  sum=sum+d**3
  temp=temp//10
if n==sum:
  print(' n is ARMSTRONG number')
else:
  print(' n is NOT ARMSTRONG number') 
# output: n:153((1+125+27=153)
n is ARMSTRONG number
n:123 (1**3+2**3+3**3=36)
n is NOT ARMSTONG number
  
