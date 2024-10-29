from Clases import *

ADN = []
n = 0
print('''
El ADN de una célula, cuenta con cuatro bases nitrogenadas:

- Adenina (A)
- Timina (T)
- Citosina (C)
- Guanina (G)

Porfavor, ingrese la correspondiente secuencia de ADN para su respectivo tratamiento:
''')

while len(ADN) < 6:
    
    user_input = input(f"Combinación número [{n+1}] de bases nitrogenadas: ")

    if len(user_input) == 6 and all(i in 'ATCG' for i in user_input):
        ADN.append(user_input)
        n += 1
    else:
        print("Cadena de bases nitrogenadas incorrecta.")

print("\n ADN ingresado correctamente: ", ADN, "\n")

n = 0
Method = Detector(n) # Instanciar

n = input('''Marque con un número ¿Que tratamiento desea realizar?\n
    1- Detectar Mutación.
    2- Sanar ADN.
    3- Mutar ADN.\n
''')

if n == '1':
    print("Detectar Mutación")
    Method.detectar_mutantes(ADN)
elif n == '2':
    print("Sanar")
elif n == '3' :
    print("Mutar ADN")
    n = input('''Marque con un número ¿Que mutación desea realziar?\n
        1- Radiación.
        2- Virus.\n
        ''')
    if(n == '1'):
        print("Radiación")
    elif(n == '2'):
        print("Virus")