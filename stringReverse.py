## Manual way to reverse the string
s= "Python Is Easy"
reversed_s = ""

for c in s.lower():
   # reversed_s = reversed_s + c  # this prints the same string again
   reversed_s = c + reversed_s  # this prints the reversal
print(reversed_s.title())


## using Slicing

s= "Python Is Easy"
reversed_s = s[::-1].lower()
print(reversed_s.title())

##  using reversed() and join ()

## using Slicing

s= "Python Is Easy"
reversed_s = "".join(reversed(s)).lower()
print(reversed_s.title())