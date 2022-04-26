# Работа с файлами на Python
import os.path

f = open(r'Laba_Newtest.txt', encoding = 'utf-8', mode='r')
n = int(input('enter the order of the number \n'))
s2 = f.readline(0)
for s2 in f:

    s1 = s2.split()

    first = 10 ** n
    second = first * 10
    Arr3 = []
    for i in range(0, len(s1)):
        s = s1[i]
        if ord(s[0]) >= 48 and ord(s[0]) <= 57:
            Arr = ''
            Arr2 = ''
            status = 0
            for y in range(0, len(s)):

                if ord(s[y]) == 44:
                    status += 1
                if ord(s[y]) >= 48 and ord(s[y]) <= 57:
                    if status == 0:
                        Arr += s[y]
                    else:
                        Arr2 += s[y]
            asd = len(Arr2)
            stroka = Arr + ',' + Arr2
            if int(Arr) >= first and int(Arr) <= second:
                s1[i] = ' '
            else:
                Arr3.append(stroka)
            # print(stroka)
    print(' '.join(s1))

# f.close()
