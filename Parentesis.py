# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

#Correctos
#arreglo = ['(', ')']
#arreglo = ['(', ')','(', ')','(', ')','(', ')','(', ')','(', ')','(', ')','(', ')','(', ')']
arreglo = ['(', '[', ']', ')', '[', ']', '(', ')']
#Incorrectos
#arreglo = [')']
#arreglo = ['(', ')', '[']
#arreglo = ['(', '(', '[', ')', ')', ']']
#arreglo = ['(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(']


stack = []
error = False

for i in range(0,len(arreglo)):
    if arreglo[i] == '(' or arreglo[i] == '[':
        stack.append(arreglo[i])
    elif arreglo[i] == ']':
        if len(stack) == 0:
            error = True
            break
        elif(stack.pop() != '['):
            error = True
            break
    elif arreglo[i] == ')':
        if len(stack) == 0:
            error = True
            break
        elif(stack.pop() != '('):
            error = True
            break

if error == False and len(stack) == 0:
    print("Sintaxis de los corchetes CORRECTA")
else:
    print("Sintaxis de los corchetes INCORRECTA")