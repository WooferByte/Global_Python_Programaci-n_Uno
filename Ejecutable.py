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
    if(Method.detectar_mutantes(ADN)):
        print("Mutaciones detectadas!")
    else:
        print("ADN sin Mutaciones!")
elif n == '2':
    print("Sanar")
elif n == '3' :
    print("Mutar ADN")
    n = input('''Marque con un número ¿Que mutación desea realziar?\n
        1- Radiación.
        2- Virus.\n
        ''')
    if n == '1':
        print("Se solicita el ingreso de la posición inicial donde se desea incertar la mutación por medio de la Radiación.")
        
        while True:
            PI = [int(x) for x in input("Ingrese dos valores (separados por espacio) entre 0 y 6: ").split()]
            if len(PI) == 2 and all(0 <= x <= 6 for x in PI):
                print("Valores válidos.")
                break
            else:
                print("Error: Debe ingresar exactamente dos valores entre 0 y 6.")

        while True:
            Orientation = input("Ingrese 'H' si desea una mutación Horizontal o 'V' si desea una mutación Vertical: ")
            if Orientation == 'H' or Orientation == 'V':
                print("Valor válido.")
                break
            else:
                print("Error: Debe ingresar 'H' o 'V' según lo deseado.")

        while True:
            base_nitrogenada = input("Ingrese la base nitrogenada con la que crear la mutación: ")
            if base_nitrogenada in 'ATCG' and len(base_nitrogenada) == 1:
                print("Valor válido.")
                break
            else:
                print("Error: La base nitrogenada debe ser A, T, C o G.")

        Radiation_Method = Radiacion(n, base_nitrogenada)
        print(Radiation_Method.crear_mutante(PI, Orientation, ADN))
        
    elif n == '2':
        print("Virus")