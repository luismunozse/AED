'''
1. Plazo fijo
Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo
por un cliente de un banco y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo,
sabiendo que el interés pactado era de 2.3% y que el banco cobra una tasa fija de gastos por servicios
financieros igual $20 por cuenta.
'''

deposito = float(input('Ingrese la cantidad de dinero a depositar en plazo fijo: '))

saldo = (deposito + (deposito * (2.3/100))) - 20

print("Saldo que tendra la cuenta al vencer el plazo fijo: ", saldo)