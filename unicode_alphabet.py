# Created on 25 oct 2016
# Created by: Matthew Lourenco
# this is a program that displays the english alphabet.
for index1 in range(65, 91):
    print(str(index1) + ' -> ' + unichr(index1))
print('----------')
for index2 in range(97, 123):
    print(str(index2) + ' -> ' + unichr(index2))
