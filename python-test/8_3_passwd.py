import re
import random
import string

def pcheck(a: str) -> str:
    res = [re.search(r"[a-z]", a), re.search(r"[A-Z]", a), re.search(r"[0-9]", a), re.search(r"\W", a)]
    if all(res):
        return "Password is okay"
    return ("Password is weak. Add "+
            "lowercase letters, "*(res[0] is None) +
            "uppercase letters, "*(res[1] is None) +
            "digits, "*(res[2] is None) +
            "special symbols, "*(res[3] is None)+
             "then try again")

password = "@12313wseAqw123"
#print(len(password))
#print(pcheck(password))


def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

test_pass = randomStringwithDigitsAndSymbols(12)
print(test_pass)
print(len(test_pass))
print(pcheck(test_pass))