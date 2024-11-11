class Detector:

    
    # Consigna Dudosa: Incluye al menos 2 atributos.
    # Consigna Dudosa: "Incluye método init con sus argumentos para definir los atributos al instanciar un objeto"

    # __init__ ¿Cumple con estas dos consignas tanto acá como en el archivo 'Ejecutable.py'?

    def __init__(self, n):
        self.n = n # Primer Atributo
        self.detection = False # Segundo Atributo

    def detectar_mutantes(self,ADN):

        # Detectar horizontales:
        for row in ADN:
            for j in range(0,5):
                if row[j] == row[j + 1]:
                    #print(f"{row[j]} es igual a {row[j+1]}")
                    self.n += 1
                    #print(self.n)  
            if self.n >= 3:
                #print("Mutación horizontal detectada!")
                #print(self.n)
                self.detection = True
                self.n = 0
                break
            else:
                self.n = 0

        if self.detection == False:
            
            # Detectar verticales:
            for j in range(0,6):
                for i in range(0,5):
                    if ADN[i][j] == ADN[i + 1][j]:
                        #print(f"La letra '{ADN[i][j]}' es igual a la letra '{ADN[i + 1][j]}'")
                        #print(f"{ADN[i]} -> {ADN[i + 1]}")}
                        self.n += 1
                        if self.n >= 3:
                            self.detection = True
                            self.n = 0
                            break
                    else:
                        #print("Diferentes")
                        self.n = 0
                if self.detection == False:
                    #print("Cambio de columna!")
                    self.n = 0
                else:
                    break

        if self.detection == False:

            # Detectar diagonales[1]:
            for i in range(0,3):
                for j in range(0,3):
                    if ADN[i][j] == ADN[i+1][j+1]: # Primera coincidencia!
                        self.n +=1
                        print(f"Letra número -> {self.n}")
                        k = i + 1 
                        l = j + 1
                        while k < 6 or l < 6:
                            print(f"¿ADN[{i}][{j}]: '{ADN[i][j]}' == ADN[{k}][{l}]: '{ADN[k][l]}'?")
                            if ADN[i][j] == ADN[k][l]:
                                self.n += 1
                                print(f"Letra número -> {self.n}")
                                if self.n >= 4: #(4) -> Cantidad de letras iguales en una misma diagonal.
                                    self.detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l += 1
                            else:
                                self.n = k = l = 0
                                print(f"No Coincidencia! -> Seteo: {self.n}")
                                break
                        if self.detection == True:
                            break
                print("Salto de Fila!")
                if self.detection == True:
                    break
            
            # Detectar diagonales[2]:
            for i in range(0,3):
                for j in range(5, 2, -1):
                    if ADN[i][j] == ADN[i+1][j-1]: # Primera coincidencia!
                        self.n +=1
                        print(f"Letra número -> {self.n}")
                        k = i + 1 
                        l = j - 1
                        while k < 6 or l < 6:
                            print(f"¿ADN[{i}][{j}]: '{ADN[i][j]}' == ADN[{k}][{l}]: '{ADN[k][l]}'?")
                            if ADN[i][j] == ADN[k][l]:
                                self.n += 1
                                print(f"Letra número -> {self.n}")
                                if self.n >= 4: #(4) -> Cantidad de letras iguales en una misma diagonal.
                                    self.detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l -= 1
                            else:
                                self.n = k = l = 0
                                print(f"No Coincidencia! -> Seteo: {self.n}")
                                break
                        if self.detection == True:
                            break
                print("Salto de Fila!")
                if self.detection == True:
                    break
        return self.detection

class Mutador:

    def __init__(self, n, base_nitrogenada):
        self.n = n
        self.base_nitrogenada = base_nitrogenada
        self.detection = False

    def crear_mutante(self):

        # Código Vacío!

        pass

class Radiacion(Mutador):
    
    def crear_mutante(self, PI, Orientation, ADN):

        print("¡Accedimos al método 'crear_mutante' dentro de Radiación!")
        print(f"PI: {PI} | Orientación: {Orientation} | ADN: {ADN} | Base Nitrogenada: {self.base_nitrogenada}")

        if Orientation == 'V':
            
            if PI[0] >= 0 and PI[0] <= 2:
                            
                print(f"Antes inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                print(f"Después inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                for i in range(1, 4):
                    print(f"Antes bucle {i} -> ADN[{PI[0] + i}][{PI[1]}] = {ADN[PI[0] + i][PI[1]]}")

                    # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                    fila = list(ADN[PI[0] + i])
                    fila[PI[1]] = self.base_nitrogenada
                    ADN[PI[0] + i] = ''.join(fila)

                    print(f"Después bucle {i} -> ADN[{PI[0] + i}][{PI[1]}] = {ADN[PI[0] + i][PI[1]]}")

            elif PI[0] >= 3 and PI[0] <= 5:

                print(f"Antes inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                print(f"Después inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                for i in range(1, 4):
                    print(f"Antes bucle {i} -> ADN[{PI[0] - i}][{PI[1]}] = {ADN[PI[0] - i][PI[1]]}")

                    # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                    fila = list(ADN[PI[0] - i])
                    fila[PI[1]] = self.base_nitrogenada
                    ADN[PI[0] - i] = ''.join(fila)

                    print(f"Después bucle {i} -> ADN[{PI[0] - i}][{PI[1]}] = {ADN[PI[0] - i][PI[1]]}")
        
        elif Orientation == 'H':

            if PI[1] >= 0 and PI[1] <= 2:
                
                print(f"Antes inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                print(f"Después inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                for i in range(1, 4):
                    print(f"Antes bucle {i} -> ADN[{PI[0]}][{PI[1] + i}] = {ADN[PI[0]][PI[1] + i]}")

                    # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                    fila = list(ADN[PI[0]])
                    fila[PI[1] + i] = self.base_nitrogenada
                    ADN[PI[0]] = ''.join(fila)

                    print(f"Después bucle {i} -> ADN[{PI[0]}][{PI[1] + i}] = {ADN[PI[0]][PI[1] + i]}")

            elif PI[1] >= 3 and PI[1] <= 5:

                print(f"Antes inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                print(f"Después inicial -> ADN[{PI[0]}][{PI[1]}] = {ADN[PI[0]][PI[1]]}")

                for i in range(1, 4):
                    print(f"Antes bucle {i} -> ADN[{PI[0]}][{PI[1] - i}] = {ADN[PI[0]][PI[1] - i]}")

                    # Convertimos la fila en una lista, realizamos la modificación y volvemos a unir
                    fila = list(ADN[PI[0]])
                    fila[PI[1] - i] = self.base_nitrogenada
                    ADN[PI[0]] = ''.join(fila)

                    print(f"Después bucle {i} -> ADN[{PI[0]}][{PI[1] - i}] = {ADN[PI[0]][PI[1] - i]}")
        
        return ADN