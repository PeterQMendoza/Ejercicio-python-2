# pedir al usuario un numero n y genere una lista con n 
# elementos con valores aleatorios y muestre como salida

from random import random

def main():
    n=int(input('Dame un numero: '))
    lst=[]
    s=0
    for i in range(0,n):
        lst.append(round(random(),3))
    for i in lst:
        s+=i
    print('La lista de {a} numeros aleatorios es: {y}'.format(a=n,y=lst))
    print('La suma de estos {s} elementos es: {r:.2f}'.format(s=n,r=s))
if __name__=='__main__':
    main()