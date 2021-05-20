def somar(num1, num2):
    n1 = str(num1)
    n2 = str(num2)
    print(n1, n2)


opcao = int(input("""\nEscolha a conversão: 
[1] Decimal > Binario
[2] Decimal > Octal
[3] Decimal > Hexadecimal
[4] Binario > Decimal
[5] Octal > Decimal
[6] Hexadecimal > Decimal
==========================
[7] Somar Binarios
[8] Subtrair Binarios
Opção: """))


if opcao == 1:
    num1 = (input('Digite o numero que deseja converter: ')).upper()
    num = int(num1)
    numAnt = num


    numConv = str(num % 2)
    num = int(num/2)
    while num > 0:
        numConv = str(num % 2) + numConv
        num = int(num/2)
    print(f'O núnumero DECIMAL: {numAnt} convertido em BINARIO é: {numConv}')

elif opcao == 2:
    num1 = (input('Digite o numero que deseja converter: ')).upper()
    num = int(num1)
    numAnt = num


    numConv = str(num % 8)
    num = int(num/8)
    while num > 0:
        numConv = str(num % 8) + numConv
        num = int(num/8)
    print(f'O núnumero DECIMAL: {numAnt} convertido em OCTAL é: {numConv}')

elif opcao == 3:
    num1 = (input('Digite o numero que deseja converter: ')).upper()
    num = int(num1)
    numAnt = num

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
    num1 = (input('Digite o numero que deseja converter: ')).upper()
    num = int(num1)
    numAnt = num

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
    num1 = (input('Digite o numero que deseja converter: ')).upper()
    num = int(num1)
    numAnt = num

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
    num1 = str(input('Digite o numero que deseja converter: ')).upper()

    num = str(num1)
    numAnt = num
    numConv = int(num, 16)
    print(f'O núnumero HEXADECIMAL: {numAnt} convertido em DECIMAL é: {numConv}')


elif opcao == 7:

    num1 = str(input("Informe o primeiro numero para ser somado: "))
    num2 = str(input("Informe o segundo numero para ser somado: "))


    r = ''
    s = 0
    resultado = ''

    i = len(num1)-1

    while i >=0:


        if (num1[i] == '0' and num2[i] == '0'):
            if (s == 0):
                r = 0
                s = 0
            else:
                r = 1
                s = 0


        if((num1[i] == '0' and num2[i] == '1') or (num1[i] == '1' and num2[i] == '0')):
            if(i!=0):
                if (s == 0):
                    r = 1
                    s = 0
                else:
                    r = 0
                    s = 1
            else:
                if(s == 1):
                    r = 10



        if(num1[i] == '1' and num2[i] == '1'):
            if(s == 0):
                if(i != 0):
                    r = 0
                    s = 1
                else:
                    r = 10
            elif(s == 1):
                if(i == 0):
                    r = 11
                else:
                    r = 1


        resultado = str(r) + resultado
        i = i-1

    print(f'\nA soma do binario {num1} + {num2} = {resultado}')

    num = int(resultado)
    numAnt = num
    n = str(num)
    numConv = 0
    pot = 0
    for i in range(len(n) - 1, -1, -1):
        calc = 2 ** pot
        pot = pot + 1
        calc2 = int(n[i]) * calc
        numConv = numConv + calc2
    print(f'O núnumero BINARIO: {numAnt} convertido em DECIMAL é: {numConv}')




elif opcao == 8:

    num1 = str(input("Informe o primeiro numero para ser somado: "))
    num2 = str(input("Informe o segundo numero para ser somado: "))

    r = ''
    s = 0
    resultado = ''
    iguala = '0'
    compl1 = ''
    compl2 = ''
    somaCompl = '1'
    conv = ''
    res = 0

    controle = len(num1)
    conv1 = len(num2)

    if(conv1 < controle):
        num2 = iguala + num2

    j = len(num2)-1
    while j >=0:
        if(num2[j] == '0'):
            conv = 1
        elif(num2[j] == '1'):
            conv = 0


        compl1 = str(conv) + compl1
        j = j - 1

    #complemento de 2
    k = len(compl1)-1
    l = k
    while k >=0:

        if (compl1[k] == '0' and somaCompl == '1'):
            if(k == l):
                r = 1
            elif(k >= 0):
                if (s == 0):
                    r = 0
                else:
                    r = 1
                    s = 0

        if (compl1[k] == '1' and somaCompl == '1'):
            if (k == l):
                r = 0
                s = 1
            elif (k >= 0):
                if (s == 0):
                    r = 1
                    s = 0
                else:
                    r = 0
                    s = 1

        compl2 = str(r) + compl2
        k = k - 1

    # Soma:
    i = len(num1)-1
    while i >= 0:

        if (num1[i] == '0' and compl2[i] == '0'):
            if (s == 0):
                r = 0
                s = 0
            else:
                r = 1
                s = 0

        if ((num1[i] == '0' and compl2[i] == '1') or (num1[i] == '1' and compl2[i] == '0')):
            if (i != 0):
                if (s == 0):
                    r = 1
                    s = 0
                else:
                    r = 0
                    s = 1
            else:
                if (s == 1):
                    r = 10

        if (num1[i] == '1' and compl2[i] == '1'):
            if (s == 0):
                if (i != 0):
                    r = 0
                    s = 1
                else:
                    r = 10
            elif (s == 1):
                if (i == 0):
                    r = 11
                else:
                    r = 1

        resultado = str(r) + resultado
        i = i - 1

    if(controle > l-1):
        resultado = resultado[1:]

    print(f'\nA soma do binario {num1} - {compl2} = {resultado}')

    num = int(resultado)
    numAnt = num
    n = str(num)
    numConv = 0
    pot = 0
    for i in range(len(n) - 1, -1, -1):
        calc = 2 ** pot
        pot = pot + 1
        calc2 = int(n[i]) * calc
        numConv = numConv + calc2
    print(f'O núnumero BINARIO: {numAnt} convertido em DECIMAL é: {numConv}')



input('\nSeu programa foi finalizado.')
