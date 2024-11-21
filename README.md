#   Proyecto de Análisis y Modificación de ADN 

**Descripción**

Este programa permite analizar y realizar tratamientos en una secuencia de ADN representada como una matriz de 6x6. El Usuario podrá:
1.	Detectar mutaciones horizontales, verticales o diagonales en la matriz de ADN.
2.	Sanar el ADN para eliminar mutaciones.
3.	Aplicar mutaciones al ADN mediante radiación o virus.
El programa está dividido en dos archivos principales:
•	Ejecutable.py: Contiene la lógica principal del programa, incluyendo la interacción con el usuario.
•	Clases.py: Define las clases necesarias para detectar y manipular la matriz de ADN.

**Archivos**

**Ejecutable.py**

Este archivo ejecuta el programa principal y realiza las siguientes funciones:
1.	Solicita al usuario ingresar 6 cadenas de bases nitrogenadas que cumplan con los requisitos:
-	Cada cadena debe tener exactamente 6 caracteres.
-	Solo se aceptan las letras A, T, C, G.
2.	Muestra la matriz de ADN ingresada en formato visual.
 	
*Esto generará una matriz como la siguiente:*

| A | T | C | G | A | T |
|---|---|---|---|---|---|
| T | T | A | G | C | T |
| C | C | G | T | A | G |
| T | A | C | T | G | A |
| G | C | T | A | T | C |
| A | G | T | C | A | G |

3.	Ofrece las siguientes opciones al usuario:

o	*Detectar mutaciones:* Usa la clase Detector para identificar secuencias repetitivas (horizontales, verticales o diagonales). Si detecta 4 letras iguales consecutivas en cualquiera de estas direcciones, indica que hay mutaciones.

o	*Sanar ADN:* Usa la clase Sanador y genera nuevas secuencias aleatorias para reemplazar las mutaciones. Continúa hasta que no se detecten mutaciones en la matriz.

o	*Mutar ADN:*

 -  Mutación por radiación: Remplaza nuevas bases nitrogenadas en una posición específica de la matriz (H o V)
 -	Mutación por virus: Remplaza nuevas bases nitrogenadas para mutarlo diagonalmente.

**Clases.py**

*Contiene las definiciones de las clases:*

•	Detector: Se encarga de analizar la matriz de ADN y detectar mutaciones:

-	Mutaciones horizontales: Cuatro o más bases consecutivas iguales en una fila.
  
-	Mutaciones verticales: Cuatro o más bases consecutivas iguales en una columna.
  
-	Mutaciones diagonales: Cuatro o más bases consecutivas iguales en una diagonal.
  
•	Mutador: Clase base para aplicar modificaciones al ADN.

•	Radiacion (hereda de Mutador): Remplazaa nuevas bases nitrogenadas en una posición y orientación específicas (horizontal o vertical).

•	Virus (hereda de Mutador): Remplaza nuevas bases nitrogenadas para mutarlo diagonalmente

•	Sanador: Crea una matriz nueva generada aleatoriamente

**Cómo usar el programa**

1.	Clona el repositorio en tu máquina local.

git clone <https://github.com/WooferByte/Global_Python_Programacion_Uno.git>

2.	Navega al directorio del proyecto:

cd <directorio>

3.	Ejecuta el archivo principal:

 **Ejecutable.py**

4.	Sigue las instrucciones en pantalla para:

-	Ingresar las cadenas de ADN.
-	Elegir la acción a realizar (detectar mutaciones, sanar ADN o aplicar mutaciones).

**Ejemplo de ejecución**

*Entrada*

El programa solicita ingresar 6 cadenas de bases nitrogenadas, por ejemplo:

ATCGAT

CGTAGC

GATCGA

ATCGAT

CGTAGC

GATCGA


*Salida* (matriz de ADN)

| A | T | C | G | A | T |
|---|---|---|---|---|---|
| C | G | T | A | G | C |
| G | A | T | C | G | A |
| A | T | C | G | A | T |
| C | G | T | A | G | C |
| G | A | T | C | G | A |

**Opciones de tratamiento**

1.	Detectar mutaciones:

-	El programa analiza y reporta mutaciones horizontales, verticales o diagonales.

2.	Sanar AND: 

-	El programa consiste en crear una matriz nueva aleatoriamente y sin mutaciones

3.	Mutar ADN:

 o	POR RADIACION:
  -	Se solicita al usuario:

     +  Posición inicial: Dos valores entre 0 y 5 que representan la fila y la columna.
     +  Orientación: Horizontal (H) o vertical (V)
     +  Base nitrogenada: Una de las letras A, T, C, G.

  o	POR VIRUS:
   - Se solicita al usuario:
     
     +	Posición inicial: Dos valores entre 0 y 5 que representan la fila y la columna.
     +	Orientacion: Diagonal.
     +	Base nitrogenada: Una de las letras A, T, C, G.

 *Autores del Proyecto:*
  
**Montuori Juan**

**Bront Facundo**

**Hanna Nicolás Naguib**
