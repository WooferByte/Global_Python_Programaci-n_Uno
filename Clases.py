class Detector:
    
    # No entiendo lo de los atributos... 
    # Consigna Pendiente: "Incluye método init con sus argumentos para definir los atributos al instanciar un objeto"

    def __init__(self, n):
        self.n = n

    def detectar_mutantes(self,ADN):
        
        detection = False

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
                detection = True
                self.n = 0
                break
            else:
                self.n = 0

        if detection == False:
            
            # Detectar verticales:
            for j in range(0,6):
                for i in range(0,5):
                    if ADN[i][j] == ADN[i + 1][j]:
                        #print(f"La letra '{ADN[i][j]}' es igual a la letra '{ADN[i + 1][j]}'")
                        #print(f"{ADN[i]} -> {ADN[i + 1]}")}
                        self.n += 1
                        if self.n >= 3:
                            detection = True
                            self.n = 0
                            break
                    else:
                        #print("Diferentes")
                        self.n = 0
                if detection == False:
                    #print("Cambio de columna!")
                    self.n = 0
                else:
                    break

        if detection == False:

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
                                    detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l += 1
                            else:
                                self.n = k = l = 0
                                print(f"No Coincidencia! -> Seteo: {self.n}")
                                break
                        if detection == True:
                            break
                print("Salto de Fila!")
                if detection == True:
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
                                    detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l -= 1
                            else:
                                self.n = k = l = 0
                                print(f"No Coincidencia! -> Seteo: {self.n}")
                                break
                        if detection == True:
                            break
                print("Salto de Fila!")
                if detection == True:
                    break
        return detection