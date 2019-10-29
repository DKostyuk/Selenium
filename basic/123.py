s = '\n' + '   Еще  ''\n' + '   q   werty  ' + '\n' + '\n' +'      123  45     7 8 9 0     ' + '\n' + '\n'
print(s)

s = s.replace('\n', ' ')
while s.find('  ') != -1:
    s = s.replace('  ', ' ')
s=s.split()
print(s)
if s[0] == 'Еще':
    s.pop(0)
ss=''
s = ' '.join(s)
print(s)
print(ss)
print(type(s))



#
# n = 3
# m = 4
# a = []
# b = []
# a.append(5)
# a.append(6)
# b.append(a)
# a = []
# a.append(45)
# b.append(a)
# print(a)
# print(b)