from random_gen import generate_random_numbers, generate_random_alphabets, generate_random_special_characters
from Crypto.Random import get_random_bytes, random


min_v=0
max_v=9

print("***** Password Generator *****")
pw_len=int(input("Enter Password Length\nRecommended to a minimum of 6\n>> ")) #user input length
print()
password_list=[]

def char_chance():
    #Generates a list of random integers within the range [0, 1, 2, 3, 4, 5, 6, 7]
    random_numbers = [random.randint(0, 7)]
    return random_numbers

for _ in range(pw_len):
    which_char=char_chance()
    print(f"{which_char} - which_char")
    if 2 in which_char or 5 in which_char:
        add_char=generate_random_special_characters(1)
        password_list.append(add_char)
    elif 0 in which_char or 1 in which_char or 4 in which_char:
        add_char=generate_random_numbers(1,min_v,max_v)
        password_list.append(add_char)
    else:
        add_char=generate_random_alphabets(1)
        password_list.append(add_char)

print(f"Generated Password list:\n{password_list}")
