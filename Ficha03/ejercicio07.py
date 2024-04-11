'''
7. Cálculo presupuestario
En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital
se reparte de la siguiente manera:

Área                Presupuesto

Urgencias               37%

Pediatría               42%

Traumatología           21%

Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que recibirá cada área.
'''

print('*' * 65)
print(' Cálculo Presupuestario ')
print('*' * 65)

presupuesto = float(input('Ingrese el presupuesto total del hospital: '))

print( 'A continuación te mostramos el monto que se destinará a cada área')
urgencias = presupuesto * 0.37
print('Urgencias: $', urgencias)
pediatria = presupuesto * 0.42
print('Pediatria: $', pediatria)
traumatologia = presupuesto * 0.21
print('Traumatologia: $', traumatologia)
