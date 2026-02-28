## find the sum of multiples of 3 from 1 to 50 

sum_m = 0
for i in range(1,51):
    if i%3 !=0:
        continue
    sum_m += i

print(sum_m)


## skip all the vowels in the given string "MaThEMaTIcS"

ch = "MaThEMaTIcS"
vowels = "aeiou"
result = ""
for letter in ch:
    if letter.lower() in vowels:
        continue
    result += letter
print(result)

## one line
print("".join(i for i in "MaThEMaTIcS" if i.lower() not in "aeiou"))