import io


def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


def spisok_name(a, b):
    nl = []
    for d, f in zip(a, b):
        nl.append([d[1:], f[1:]])
        return nl

with io.open('task_file.txt', 'r') as file:
    for line in file:
        words = file.readline().split(',')
        try:
            name = [words[1]]
            last_name = [words[2]]
            if words[3].startswith(' 7') == True:
                print(email_gen(spisok_name(name, last_name)))

        except IndexError:
            print('Error - Index')


