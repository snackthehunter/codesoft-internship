#simple calculator

#taking numbers as input from user
fnum= int(input('Enter the first number\t:'))
snum= int(input('Enter the second number\t:'))

#taking operation as an input from user
op= input('Choose one option from the following- \n 1 for additon, \n 2 for subtraction, \n 3 for multiplication, \n 4 for division, \n 5 for modulos,\n')

#operating operands

if op == '1':
    print( fnum+snum)
elif op == '2':
    print(fnum-snum)
elif op == '3':
    print(fnum*snum)
elif op == '4':
    if fnum == 0 and snum == 0:
        print('indeterminant form')
    elif fnum != 0 and snum == 0:
        print('invalid entry')
    else:
        print(fnum/snum)
else:
    print(fnum%snum)