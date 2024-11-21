import random

class Detector:

    def __init__(self, n):
        self.n = n
        self.detection = False

    def detectar_mutantes(self,ADN):

        self.detection = False

        for row in ADN:
            for j in range(0,5):
                if row[j] == row[j + 1]:
                    self.n += 1
                    if self.n >= 3:
                        break
                else:
                    self.n = 0
            if self.n >= 3:
                self.detection = True
                self.n = 0
                break
            else:
                self.n = 0

        if self.detection == False:
            
            for j in range(0,6):
                for i in range(0,5):
                    if ADN[i][j] == ADN[i + 1][j]:
                        self.n += 1
                        if self.n >= 3:
                            self.detection = True
                            self.n = 0
                            break
                    else:
                        self.n = 0
                if self.detection == False:
                    self.n = 0
                else:
                    break

        if self.detection == False:

            for i in range(0,3):
                for j in range(0,3):
                    if ADN[i][j] == ADN[i+1][j+1]:
                        self.n +=1
                        k = i + 1 
                        l = j + 1
                        while k < 6 or l < 6:
                            if ADN[i][j] == ADN[k][l]:
                                self.n += 1
                                if self.n >= 4:
                                    self.detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l += 1
                            else:
                                self.n = k = l = 0
                                break
                        if self.detection == True:
                            break
                if self.detection == True:
                    break
            
            for i in range(0,3):
                for j in range(5, 2, -1):
                    if ADN[i][j] == ADN[i+1][j-1]:
                        self.n +=1
                        k = i + 1 
                        l = j - 1
                        while k < 6 or l < 6:
                            if ADN[i][j] == ADN[k][l]:
                                self.n += 1
                                if self.n >= 4:
                                    self.detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l -= 1
                            else:
                                self.n = k = l = 0
                                break
                        if self.detection == True:
                            break
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

        if Orientation == 'V':
            
            if PI[0] >= 0 and PI[0] <= 2:

                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                for i in range(1, 4):

                    fila = list(ADN[PI[0] + i])
                    fila[PI[1]] = self.base_nitrogenada
                    ADN[PI[0] + i] = ''.join(fila)

            elif PI[0] >= 3 and PI[0] <= 5:

                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                for i in range(1, 4):

                    fila = list(ADN[PI[0] - i])
                    fila[PI[1]] = self.base_nitrogenada
                    ADN[PI[0] - i] = ''.join(fila)
        
        elif Orientation == 'H':

            if PI[1] >= 0 and PI[1] <= 2:

                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                for i in range(1, 4):

                    fila = list(ADN[PI[0]])
                    fila[PI[1] + i] = self.base_nitrogenada
                    ADN[PI[0]] = ''.join(fila)

            elif PI[1] >= 3 and PI[1] <= 5:

                fila = list(ADN[PI[0]])
                fila[PI[1]] = self.base_nitrogenada
                ADN[PI[0]] = ''.join(fila)

                for i in range(1, 4):

                    fila = list(ADN[PI[0]])
                    fila[PI[1] - i] = self.base_nitrogenada
                    ADN[PI[0]] = ''.join(fila)
        
        return ADN

class Virus(Mutador):

    def crear_mutante(self, PI, ADN):

        if PI[1] in range(0, 3):

            if PI[0] in range(0, 3):
                
                for k in range(0, 4):
                    fila = list(ADN[PI[0] + k])
                    fila[PI[1] + k] = self.base_nitrogenada
                    ADN[PI[0] + k] = ''.join(fila)
            
            if PI[0] in range(3, 6):
                
                for k in range(0, 4):
                    fila = list(ADN[PI[0] - k])
                    fila[PI[1] + k] = self.base_nitrogenada
                    ADN[PI[0] - k] = ''.join(fila)

        if PI[1] in range(3, 6):
            
            if PI[0] in range(0, 3):
                for k in range(0, 4):
                    fila = list(ADN[PI[0] + k])
                    fila[PI[1] - k] = self.base_nitrogenada
                    ADN[PI[0] + k] = ''.join(fila)
            
            if PI[0] in range(3, 6):
                for k in range(0, 4):
                    fila = list(ADN[PI[0] - k])
                    fila[PI[1] - k] = self.base_nitrogenada
                    ADN[PI[0] - k] = ''.join(fila)
        return ADN
    
class Sanador:

    def __init__(self, n):
        self.n = n
        self.detection = False

    def Detectar_Mutantes(self, ADN):

        for row in ADN:
            for j in range(0,5):
                if row[j] == row[j + 1]:
                    self.n += 1
                    if self.n >= 3:
                        break
                else:
                    self.n = 0
            if self.n >= 3:
                self.detection = True
                self.n = 0
                break
            else:
                self.n = 0

        if self.detection == False:
            
            for j in range(0,6):
                for i in range(0,5):
                    if ADN[i][j] == ADN[i + 1][j]:
                        self.n += 1
                        if self.n >= 3:
                            self.detection = True
                            self.n = 0
                            break
                    else:
                        self.n = 0
                if self.detection == False:
                    self.n = 0
                else:
                    break

        if self.detection == False:

            for i in range(0,3):
                for j in range(0,3):
                    if ADN[i][j] == ADN[i+1][j+1]:
                        self.n +=1
                        k = i + 1 
                        l = j + 1
                        while k < 6 or l < 6:
                            if ADN[i][j] == ADN[k][l]:
                                self.n += 1
                                if self.n >= 4:
                                    self.detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l += 1
                            else:
                                self.n = k = l = 0
                                break
                        if self.detection == True:
                            break
                if self.detection == True:
                    break
            
            for i in range(0,3):
                for j in range(5, 2, -1):
                    if ADN[i][j] == ADN[i+1][j-1]:
                        self.n +=1
                        k = i + 1 
                        l = j - 1
                        while k < 6 or l < 6:
                            if ADN[i][j] == ADN[k][l]:
                                self.n += 1
                                if self.n >= 4:
                                    self.detection = True
                                    self.n = 0
                                    break
                                k += 1
                                l -= 1
                            else:
                                self.n = k = l = 0
                                break
                        if self.detection == True:
                            break
                if self.detection == True:
                    break
        return self.detection
    
    def sanar_mutantes(self, ADN):

            if self.Detectar_Mutantes(ADN):
                
                print("Se han detectado mutaciones! Procediendo a sanar...")
                
                for m in range(10):

                    ADN = [''.join(random.choices('ATCG', k=6)) for _ in range(6)]
                    
                    self.n = 0
                    self.detection = False
                    
                    if not self.Detectar_Mutantes(ADN):
                        print("Matriz sanada generada con éxito!")
                        return ADN
                    
                    elif m >= 9:
                        print("Matriz sanada no generada! Porfavor inténtelo de nuevo.")
                        return ADN
            else:
                print("No se detectaron mutaciones para sanar!")
                return ADN