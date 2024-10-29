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
        return detection