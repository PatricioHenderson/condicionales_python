#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1= float(input("Ingrese el primer numrero: \n"))
    numero_2= float(input("Ingrese el segundo numrero: \n"))

    numero_3= numero_1 - numero_2

    if numero_3 > 0 :
        
        print("El resultlado es positivo ")

    elif numero_3 < 0 :

        print("El resultado es negativo")

    elif numero_3 == 0 :

        print("El resultado es cero")
def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input("Ingrese el primer numero: "))

    numero_2 = int(input("Ingrese el segundo numero: "))
    
    numero_3 = int(input("Ingrese el tercer numero: "))

    #Buscamos el resto de la división sobre 2 para saber si son pares.
    numero_4 = numero_1 % 2

    numero_5 = numero_2 % 2

    numero_6 = numero_3 % 2
    
    if numero_4 == 0:
        print ("{} Es par" .format(numero_1) ) 
    
    else:

        print ("{} Es impar" .format(numero_1) )  
    
    if numero_5 == 0:

        print ("{} Es par" .format(numero_2) )
    
    else:

        print ("{} Es impar" .format(numero_2) )  
    
    if numero_6 == 0:

        print ("{} Es par" .format(numero_3) ) 

    else:

        print ("{} Es impar" .format(numero_3) )       

def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_1 = float(input("Introducir primer numero: "))
    
    numero_2 = float(input("Introducir segundo numero: "))
    
    funcion = str(input("Introducir simbolo operación a realizar "))

    if funcion == "+" :

        print ("el resultado es : " , numero_1 + numero_2)
    
    elif funcion == "-" :

        print ("el resultado es : ", numero_1 - numero_2)

    elif funcion == "*" :

        print ("el resultado es : ", numero_1 * numero_2)

    elif funcion == "/" :

        print ("el resultado es : ", numero_1 / numero_2)
    
    elif funcion == "**" :

        print ("el resultado es : ", numero_1 ** numero_2)

    else :

        print ("Indrodujo una transacción no soportada")


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palabra_1= str(input("Introducir primer palabra: "))
    palabra_2= str(input("Introducir segunda palabra: "))
    palabra_3= str(input("Introducir tercer palabra: "))
    #Creamos la lista
    lista =  palabra_1.lower() , palabra_2.lower() , palabra_3.lower()
    #Ponemos todo en minusculas para que luego queden bien ordenadas
    #¿Acá la consulta es si puedo ponerlas todas en minuscula sin ponerles 
    #.lower al final porque quise hacerlo como esta abajo y me tiro errror.
    #lista_2= lista.lower()

    orden = int(input("Elegir 1 para orden alfabético o 2 para ordear por cantidad  de letras: "))
    #Acá si apreto enter para no escribir más de 80 caracteres me separa, no se como hacer para
    # que continue dentro del parentesis

    if orden == 1 :

        lista_orden = sorted(lista)
        print (lista_orden)
    
    elif orden == 2 :

        lista_orden = sorted(lista, key=len , reverse=True)

        print (lista_orden)

    else:

        print("Selección incorrecta.")

def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    from statistics import mean

    temp_1= float(input("Ingresar temperatura 1 : "))
    
    temp_2= float(input("Ingresar temperatura 2 : "))
    
    temp_3= float(input("Ingresar temperatura 3 : "))

    temperaturas = (temp_1 , temp_2 , temp_3)

    eleccion = int(input("Seleccione 1 para ver la máxima, 2 para ver la minima y 3 para ver el promedio "))

    if eleccion == 1 :
        
        print ("La máxima es " , max(temperaturas)  )
    
    if eleccion == 2 :

        print ("La minima es " , min(temperaturas) )
    
    if eleccion == 3 :
    
        print ("El promedio es " , mean(temperaturas))

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
