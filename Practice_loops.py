# ## Print the multiplication table of 5 using a while loop.

# i=1
# while i<= 10:
#     m = 5*i
#     print("5 * ", i, "=", m)
#     i+= 1

# ## Use a while loop to print even numbers from 2 to 10.

# i = 2
# while i<= 10:
#     print(i)
#     i+=2

# ## Use a for loop to print each character in the string "Python".

# string = "Python"
# for Character in string:
#     print(Character)

## sum and count of Prime numbers from 1 to 100 

sum_prime = count_prime = 0
for i in range(2,101):
    is_prime = True
    for j in range (2, i+1):
        if i%j == 0:
            is_prime = False
            break
    if is_prime == True:
        sum_prime += i 
        count_prime += 1
    i +=1  

print("Sum:", sum_prime)
print("Count:", count_prime)

# sum_prime = 0
# count_prime = 0

# for n in range(2, 101):
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         sum_prime += n
#         count_prime += 1

# print("Sum:", sum_prime)
# print("Count:", count_prime)
