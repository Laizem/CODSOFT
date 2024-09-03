import string
from Crypto.Random import get_random_bytes, random

def generate_random_numbers(count, min_value, max_value):

    random_bytes = get_random_bytes(count * 4)  # 4 bytes per integer
    random_integers = [int.from_bytes(random_bytes[i:i+4], byteorder='big') % (max_value - min_value + 1) + min_value for i in range(0, len(random_bytes), 4)]
    return random_integers

def generate_random_alphabets(length):

    alphabets = string.ascii_letters  # Includes both uppercase and lowercase letters
    random_indices = [random.randint(0, len(alphabets) - 1) for _ in range(length)]
    random_alphabets = ''.join(alphabets[i] for i in random_indices)
    return random_alphabets

def generate_random_special_characters(length):
    special_characters = string.punctuation  # Includes all punctuation characters
    random_indices = [random.randint(0, len(special_characters) - 1) for _ in range(length)]
    random_special_characters = ''.join(special_characters[i] for i in random_indices)
    return random_special_characters