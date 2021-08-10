#David Hernán García Fernández - A01173130

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

"""Casos de prueba"""
#Correctos
#arreglo = ['(', ')']
#arreglo = ['(', ')','(', ')','(', ')','(', ')','(', ')','(', ')','(', ')','(', ')','(', ')']
arreglo = ['(', '[', ']', ')', '[', ']', '(', ')']
#Incorrectos
#arreglo = [')']
#arreglo = ['(', ')', '[']
#arreglo = ['(', '(', '[', ')', ')', ']']
#arreglo = ['(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(','(']

def parentesis (arreglo):
    """Función que recibe un arreglo de caracteres y revisa si los corchetes que se abrieron se cerraron.
    Regresa True cuando encuentra errores de sintaxis en los corchetes, es decir, si alguno se abrió y
    nunca se cerró o si se cerró sin abrirse"""
    stack = []
    for i in range(0,len(arreglo)): #Recorre el arreglo
        if arreglo[i] == '(' or arreglo[i] == '[':
            stack.append(arreglo[i]) #Guarda los corchetes en el Stack
        elif arreglo[i] == ']':
            if len(stack) == 0: #Si el stack está vacío y encontró un corchete cerrado es porque falta uno de apertura
                return True #True implica que la sintaxis es incorrecta
            elif(stack.pop() != '['): #Si no extrae el de apertura esperado
                return True
        elif arreglo[i] == ')':
            if len(stack) == 0:
                return True
            elif(stack.pop() != '('):
                return True
    if len(stack) == 0: #Verifica que el Stack esté vacío al terminar las iteraciones. No estar vacío implica que abró un corchete que nunca cerró
        return False
    else: 
        return True


if parentesis(arreglo) == False:
    print("Sintaxis CORRECTA en los corchetes")
else:
    print("Sintaxis INCORRECTA en los corchetes")