def somar(num1, num2):
    lista1 = num1.split()
    print(lista1)

num1 = (input('Digite o numero que deseja converter: ')).upper()
opcao = int(input("""\nEscolha a conversão: 
[1] Decimal > Binario
[2] Decimal > Octal
[3] Decimal > Hexadecimal
[4] Binario > Decimal
[5] Octal > Decimal
[6] Hexadecimal > Decimal
[7] Somar Binarios
Opção: """))


if str(num1) and opcao <6:
    num = int(num1)
    numAnt = num

    if opcao == 1:
        numConv = str(num % 2)
        num = int(num/2)
        while num > 0:
            numConv = str(num % 2) + numConv
            num = int(num/2)
        print(f'O núnumero DECIMAL: {numAnt} convertido em BINARIO é: {numConv}')

    elif opcao == 2:
        numConv = str(num % 8)
        num = int(num/8)
        while num > 0:
            numConv = str(num % 8) + numConv
            num = int(num/8)
        print(f'O núnumero DECIMAL: {numAnt} convertido em OCTAL é: {numConv}')

    elif opcao == 3:
        numConv = int(num % 16)
        if numConv > 9:
            a = 1
            if numConv == 10:
                numConv = 'A'
            if numConv == 11:
                numConv = 'B'
            if numConv == 12:
                numConv = 'C'
            if numConv == 13:
                numConv = 'D'
            if numConv == 14:
                numConv = 'E'
            if numConv == 15:
                numConv = 'F'
        else:
            numConv = str(num % 16)

        num = int(num / 16)
        while num > 0:
            numAdd = int(num % 16)
            if numAdd > 9:
                a=1
                if numAdd == 10:
                    numAdd = 'A'
                if numAdd == 11:
                    numAdd = 'B'
                if numAdd == 12:
                    numAdd = 'C'
                if numAdd == 13:
                    numAdd = 'D'
                if numAdd == 14:
                    numAdd = 'E'
                if numAdd == 15:
                    numAdd = 'F'
            else:
                numAdd = str(num % 16)
            #print(numAdd)
            numConv = numAdd + numConv
            num = int(num / 16)
        print(f'O núnumero DECIMAL: {numAnt} convertido em HEXADECIMAL é: {numConv}')

    elif opcao == 4:
        n = str(num)
        numConv = 0
        pot = 0
        for i in range(len(n)-1, -1, -1):
            calc = 2 ** pot
            pot = pot + 1
            calc2 = int(n[i]) * calc
            numConv = numConv + calc2
        print(f'O núnumero BINARIO: {numAnt} convertido em DECIMAL é: {numConv}')

    elif opcao == 5:
        n = str(num)
        numConv = 0
        pot = 0
        for i in range(len(n)-1, -1, -1):
            calc = 8 ** pot
            pot = pot + 1
            calc2 = int(n[i]) * calc
            numConv = numConv + calc2
        print(f'O núnumero OCTAL: {numAnt} convertido em DECIMAL é: {numConv}')


elif opcao == 6:
    num = str(num1)
    numAnt = num
    numConv = int(num, 16)
    print(f'O núnumero HEXADECIMAL: {numAnt} convertido em DECIMAL é: {numConv}')


"""if opcao == 7:

    num1 = int(input("Informe o primeiro numero para ser somado: "))
    num2 = int(input("Informe o segundo numero para ser somado: "))
    somar(num1, num2)"""


input('\nSeu programa foi finalizado.')
