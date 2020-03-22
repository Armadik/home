 def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

with open('task_file.txt', 'r') as file:
    words = file.read().split(',')
    name = (words[1::4])
    last_name = (words[2::4])
    tel = (words[3::4])
    city = (words[4::4])

for f in tel:
    if f[0:2] == ' 7':
        print(f)
    else:
        'no do'
