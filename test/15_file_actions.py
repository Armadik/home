import io

################################################################
def email_gen(list_of_names):
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
#################################################################


with io.open('task_file.txt', 'r') as file:
    for line in file:
        words = file.read().split(',')
        name = (words[1::4])
        last_name = (words[2::4])
        tel = (words[3::4])
        city = (words[4::4])
        with open('test-test', 'w') as new_file:
            new_file.write(str(line))
        for t, n, l, c in zip(tel, name, last_name, city):
            if t[0:2] == ' 7':
                mail = email_gen(spisok_name([n], [l]))
                lin1 = (str(mail[0]), t, n, l, c[:-1])
                with open('test-test', 'a') as new_file:
                    new_file.write(str(lin1) + '\n')
            else:
                lin2 = ('no mail', t, n, l, c[:-1])
                with open('test-test', 'a') as new_file:
                    new_file.write(str(lin2) + '\n')







