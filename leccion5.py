"""
la funcion valida que si el resto de 4 con  del valor indicado por el usuario
es 0 entonces es bisiesto
"""


def esBisiesto(year):
    if year % 4 == 0:
        return 'Bisiesto'
    else:
        return 'No es Bisiesto'


# programa principal
yearInput = int
print('Bienvenido')
while True:
    try:
        yearInput = int(input('Por favor ingresa el año a validar. '))
        print('El año que ingresaste es:', esBisiesto(yearInput))
        break
    except:
        print('Error:por favor ingresa un año valido!!!')

print('Fin del programa')
