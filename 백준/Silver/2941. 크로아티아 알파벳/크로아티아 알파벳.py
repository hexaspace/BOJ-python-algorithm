import re

sent = input().rstrip()

kro1 = re.compile('c=')
kro2 = re.compile('c-')
kro3 = re.compile('dz=')
kro4 = re.compile('d-')
kro5 = re.compile('lj')
kro6 = re.compile('nj')
kro7 = re.compile('s=')
kro8 = re.compile('z=')

count = len(sent)
count -= len(kro1.findall(sent))
count -= len(kro2.findall(sent))
count -= len(kro3.findall(sent))  # dz=에서 하나 찾으면, z=에서 한번 더 찾아짐
count -= len(kro4.findall(sent))
count -= len(kro5.findall(sent))
count -= len(kro6.findall(sent))
count -= len(kro7.findall(sent))
count -= len(kro8.findall(sent))
print(count)