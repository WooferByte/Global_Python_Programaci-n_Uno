class Detector:
    
    # No entiendo lo de los atributos... 
    # Consigna Pendiente: "Incluye método init con sus argumentos para definir los atributos al instanciar un objeto"

    def __init__(self, n):
        self.n = n

    def detectar_mutantes(self,ADN):
        
        # Detectar horizontales:
        for row in ADN:
            for j in range(0,5):
                if row[j] == row[j + 1]:
                    print(f"{row[j]} es igual a {row[j+1]}")
                    self.n += 1
                    print(self.n)  
            if self.n >= 4:
                print("Mutación horizontal detectada!")
                print(self.n)
                self.n = 0
            else:
                self.n = 0