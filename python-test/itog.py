import io
import re
import random
import string


################################################################
def email_gen(list_of_names):
    '''Create mail'''
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


def spisok_name(a, b):
    '''Comment :)'''
    nl = []
    for d, f in zip(a, b):
        nl.append([d[1:], f[1:]])
        return nl


def pcheck(a: str) -> str:
    '''Check passowd'''
    res = [re.search(r"[a-z]", a), re.search(r"[A-Z]", a), re.search(r"[0-9]", a), re.search(r"\W", a)]
    if all(res):
        return "Password is okay"
    return ("Password is weak. Add "+
            "lowercase letters, "*(res[0] is None) +
            "uppercase letters, "*(res[1] is None) +
            "digits, "*(res[2] is None) +
            "special symbols, "*(res[3] is None)+
             "then try again")


def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

#################################################################

# Create files - valid_users and no_valid_users fron task_file
with io.open('task_file.txt', 'r') as file:
    for line in file:
        words = file.read().split(',')
        name = (words[1::4])
        last_name = (words[2::4])
        tel = (words[3::4])
        city = (words[4::4])
        # Clears files
        with open('valid_users.txt', 'w') as new_file:
            print("Create/clean valid_user.txt")
            new_file.write(str(line))
        with open('no_valid_users.txt', 'w') as new_file:
            print("Create/clean no_valid_users.txt")
            new_file.write(str(line))
        for t, n, l, c in zip(tel, name, last_name, city):
            if t[0:2] == ' 7':
                mail = email_gen(spisok_name([n], [l]))
                lin1 = (str(mail[0]), t, n, l, c[:-1])
                # tyt podumat' ewe
                if l == ' ':
                    with open('no_valid_users.txt', 'a') as new_file:
                        new_file.write((str(',') + str(n + ',') + str(l + ',') + str(t + ',') + str(c[:-1]) + '\n'))
                else:
                    print('Create:', mail)
                    with open('valid_users.txt', 'a') as new_file:
                        new_file.write((str(mail[0]+',') + str(n+',') + str(l+',') + str(t+',') + str(c[:-1]) + '\n'))
            else:
                lin2 = ('no mail', t, n, l, c[:-1])
                with open('no_valid_users.txt', 'a') as new_file:
                    new_file.write((str(',') + str(n+',') + str(l+',') + str(t+',') + str(c[:-1]) + '\n'))


with open('valid_users.txt', 'r') as users_file:
    with open('valid_users_password.txt', 'w') as users_file_pass:
        users_file_pass.write(str(line[:-1] + ', PASSWORD\n'))
    for u in users_file.readlines():
        if re.findall(r'@', u):
            print('Create password for mail :', re.findall(r'\w+\.\w+\@\w+', u))
            password_mail = randomStringwithDigitsAndSymbols(12)
            with open('valid_users_password.txt', 'a') as users_file_pass:
                users_file_pass.write(u[:-1] +', '+password_mail+'\n')
