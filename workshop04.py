__author__ = 'sci-lmw1'

# Example to Study

# import random
#
# MAX_INCREASE = 0.1 # 10%
# MAX_DECREASE = 0.05 # 5%
# MIN_PRICE = 0.01
# MAX_PRICE = 1000.0
# INITIAL_PRICE = 10.0
#
#
# def format_currency(value):
#     return "$" + format(price, ".2f")
#
# price = INITIAL_PRICE
# day = 0
# print("Starting price:", format_currency(price))
#
# while price >= MIN_PRICE and price <= MAX_PRICE:
#     priceChange = 0
#     day += 1
#     # generate a random integer of 1 or 2
#     # if it's 1, the price increases, otherwise it decreases
#     if random.randint(1, 2) == 1:
#         # generate a random floating-point number
#         # between 0 and MAX_INCREASE
#         priceChange = random.uniform(0, MAX_INCREASE)
#     else:
#         # generate a random floating-point number
#         # between negative MAX_INCREASE and 0
#         priceChange = random.uniform(-MAX_DECREASE, 0)
#
#     price *= (1 + priceChange)
#     print("On day", day, "price is:", format_currency(price))
#
#


# Example 2 - Word generator

# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#
# word_format = "ccvcvc"
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     else:
#         word += random.choice(VOWELS)
#
# print(word)


# Password checker

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    countLower = 0
    countUpper = 0
    countDigits = 0
    countSpecial = 0
    for char in password:
        if char.isdigit():
            countDigits += 1
        elif char.islower():
            countLower += 1
        elif char.isupper():
            countUpper += 1
        elif char in SPECIALS:
            countSpecial += 1
        else:
            pass

    if countLower == 0 or countUpper == 0 or countDigits == 0:
        return False
    if SPECIAL_CHARS_REQUIRED:
        if countSpecial == 0:
            return False
    return True

main()



# def is_valid_number(user_input, lower, upper):
#         if not user_input.isdecimal():
#            print("error - not a number")
#            continue
#         number = int(user_input)
#         if number < start or number > end:
#            print("error - outside range")
#            continue
#         return number
#
#
# def generate_query(min, max):
#     return"Enter a number (" + str(min) + "-" + str(max) + "):"
#
# def get_number(start, end):
#         user_input = input(generate_query(start, end))
#         while not is_valid_number(start, end):
#             print("Invalid number")
#             user_input = input(generate_query(start, end))

