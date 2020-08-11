import random
import string
import math
#Modules 
#Object oriented programing
#Class Work

print("Working with Imports")
for i in range(7):
    print(random.randint(1,49))



def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(8)
get_random_string(8)
get_random_string(6)

print("From Statement """)

#print(math.sqrt(input("Enter a number having a multiple of any size: ")))


print("The DIR() Statement")

print(dir(string))

