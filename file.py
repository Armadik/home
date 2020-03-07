#!/usr/bin/env python3.5
f = open('data.txt', 'w') # Создаем новый файл
f.write('Hello\n')
f.write('word\n')
f.close()

f = open('data.txt')
text = f.read()

print(text)
text.split()

for line in open('data.txt', 'r'):
    print(line, end='')