import io

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

#################################################################

with io.open('task_file.txt', 'r') as file:
    for line in file:
        words = file.read().split(',')
        name = (words[1::4])
        last_name = (words[2::4])
        tel = (words[3::4])
        city = (words[4::4])

index = 0
for d, f in zip(name, last_name):
    index += 1
#    print(d+'_'+str(index), f+'_'+str(index))
    nl = []
    nl.append(d[1:]+'_'+str(index)+','+f+'_'+str(index))
    print(nl)

