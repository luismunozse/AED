#1. Cuadrados y cubos

#Leer dos números y calcular:
    #La suma de sus cuadrados.
    #El promedio de sus cubos.

#Importamos interfaz gráfica
import PySimpleGUI as psg

#Pedimos el ingreso de los números
num1 = float(psg.popup_get_text('Ingrese el primer numero', 'Datos'))
num2 = float(psg.popup_get_text('Ingrese el segundo numero', 'Datos'))

#Calculamos la suma de sus cuadrados
sum = (num1**2 + num2**2)

#Calculamos el promedio de sus cubos
prom = (num1**3 + num2**3) / 2

psg.popup('La suma de los cuadrados es: ', sum , 'El promedio de los cubos es: ', prom)
