# palindrome program
i = input('i:')
i = i.casefold() # caseflod() method is returns a string where all the characters are lower case.
r = reversed(i)
if list(i) == list(r):
    print('palindrome')
else:
    print('not a palindrome')
# using slicing, palindrome check whether it is or not
s = input('s:')
rev = s[::-1] # slicing operation used s[start:end:increment/decrement]
if rev == s:
    print('palindrome')
else:
    print('not a palindrome')

# using while loop whether the given input is palindrome or not
i =int(input('i:'))
temp =i #temperary variable assigne the value of i
rev= 0
while i>0:
    rem =i%10 
    rev =rev*10+rem
    i = i//10
if temp==rev:
    print('palindrome')
else:
    print('not a palindrome')
