import re

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
print(len(password))
print(pcheck(password))
