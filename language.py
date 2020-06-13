file = open('test1.txt',  encoding='utf-8')

d = file.readlines()

language = input("Enter your language: 'EN' 'HY' 'RU' ")
language = language.upper()

if language == "EN":
    print(d[0].strip())
elif language == 'HY':
    print(d[1].strip())
elif language == 'RU':
    print(d[2].strip())

file.close()