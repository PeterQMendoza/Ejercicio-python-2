# Ejercicio 3: pedir al usuario su fecha de macimiento y 
# responder el dia de la semana correspondiente.

def main():
    sum_days=0
    sum_to_day=0

    day_on_week={0:'domingo',1:'lunes',2:'martes',3:'miercoles',
                 4:'jueves',5:'viernes',6:'sabado'}
    month_on_year_bisiesto={0:31,1:29,2:31,3:30,4:31,5:30,6:31,7:31,
                            8:30,9:31,10:30,11:31}
    month_on_year={0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,
                            8:30,9:31,10:30,11:31}

    d=str(input('Introduce tu fecha de nacimiento (DD-MM-YYYY) :'))
    day=int(d.split('-')[0])
    month=int(d.split('-')[1])
    year=int(d.split('-')[2])
    
    # Calculo de dia que inicia cada a;o
    n=6 # Inicio de los tiempos (Calibracion)
    a=0
    while(a<year):
        n=(n+1)%7
        if(a%4 is 0) and a is not 0:
            n=(n+1)%7
        a+=1

    # A;o bisiesto
    if(year%4 is 0):
        for i in range(month-1):
            sum_days+=list(month_on_year_bisiesto.values())[i]
    else:
        for i in range(month-1):
            sum_days+=list(month_on_year.values())[i]
    print('Naciste en: ',day_on_week[(sum_days+day+n-1)%7])


if __name__=='__main__':
    main()
