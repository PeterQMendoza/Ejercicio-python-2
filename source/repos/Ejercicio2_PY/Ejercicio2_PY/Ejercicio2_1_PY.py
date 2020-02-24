# Ejercicio 1:Pedir una cadena. A continuacion pedir otra
# buscar la segunda cadena en la primera ignorar mayuculas
# y minusculas

def main():
    cdn1=str(input('Cadena 1: ')).lower()
    cdn2=str(input('Cadena 2: ')).lower()
    if cdn2 in cdn1:
        print('La segunda cadena es una subcadena de la primera')
    else:
        print('La segunda cadena no es una subcadena de la primera')

if __name__=='__main__':
    main()