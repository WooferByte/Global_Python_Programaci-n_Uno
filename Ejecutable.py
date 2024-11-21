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
Method = Detector(n)

while True:

    print("Matriz 6x6 (ADN):")
    for fila in ADN:
        print(" ".join(fila))

    opcion = input('''\nMarque con un número ¿Qué tratamiento desea realizar?\n
    1- Detectar Mutación.
    2- Sanar ADN.
    3- Mutar ADN.
    4- Salir.\n
    Opción -> ''')

    if opcion == '1':
        if(Method.detectar_mutantes(ADN)):
            print("Mutaciones detectadas!")
        else:
            print("ADN sin Mutaciones!")
    elif opcion == '2':
        
        Heal = Sanador(n)  
        ADN = Heal.sanar_mutantes(ADN)

    elif opcion == '3' :
        subOpcion = input('''Marque con un número ¿Que mutación desea realziar?\n
            1- Radiación.
            2- Virus.\n
            Opción -> ''')
        if subOpcion == '1':
            print("Se solicita el ingreso de la posición inicial donde se desea incertar la mutación por medio de la Radiación.")
            
            while True:
                PI = [int(x) for x in input("Ingrese dos valores (separados por espacio) entre 0 y 5: ").split()]
                if len(PI) == 2 and all(0 <= x <= 5 for x in PI):
                    print("Valores válidos.")
                    break
                else:
                    print("Error: Debe ingresar exactamente dos valores entre 0 y 5.")

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
            ADN = Radiation_Method.crear_mutante(PI, Orientation, ADN)
            
        elif subOpcion == '2':
            print("Se solicita el ingreso de la posición inicial donde se desea incertar la mutación Virus.")
            
            while True:
                PI = [int(x) for x in input("Ingrese dos valores (separados por espacio) entre 0 y 5: ").split()]
                if len(PI) == 2 and all(0 <= x <= 5 for x in PI):
                    print("Valores válidos.")
                    break
                else:
                    print("Error: Debe ingresar exactamente dos valores entre 0 y 5.")

            while True:
                base_nitrogenada = input("Ingrese la base nitrogenada con la que crear la mutación: ")
                if base_nitrogenada in 'ATCG' and len(base_nitrogenada) == 1:
                    print("Valor válido.")
                    break
                else:
                    print("Error: La base nitrogenada debe ser A, T, C o G.")
            
            Virus_Method = Virus(n, base_nitrogenada)
            ADN = Virus_Method.crear_mutante(PI, ADN)

    elif opcion == '4':
        print("¡Gracias por usar el programa! Hasta luego.")
        break