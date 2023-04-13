import re


# Email Detector
# Regex command to find occurrence of an email in a given string

def email_detector(text):
    # regex command for the email
    f = "([a-zA-Z0-9]+)@([a-z]+).([a-z]+)"
    # Search for the email
    email = re.search(f"{f}", text)
    return email.group()


txt = "This is an example email address, 'test65@yahoo.com'. For test."
print(email_detector(txt))


# Password generator
# An algorith to generate a strong password, hash it then save it for future reference

def password_gen(password_length):
    # import necessary modules
    import random, string

    # define the characters to be used
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    special_chars2 = "!@#$%&*_-+:?|;.,"

    charset = letters + digits + special_chars
    charset2 = letters + digits + special_chars2
    # print(charset)
    # print(charset2)

    password = []
    for i in range(password_length):
        n = random.choice(charset2)
        password.append(n)

    password = "".join(password)
    return password


def password_encrypt(password):
    import hashlib

    password = hashlib.sha256(password.encode()).hexdigest()
    return password


pass_length = input()
p = password_encrypt(password_gen(pass_length))
print(p)