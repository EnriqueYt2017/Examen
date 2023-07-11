import funciones as fun
import numpy as np
from colorama import Fore,Style,Back, init
init()
init(autoreset=True)
#Len=Largo

epla=120000
egol=80000
esil=50000

Rut=[]

x=0
cepla=0
cegol=0
cesil=0
totalp=0
totalg=0
totals=0
rut=None
asientoO='🔴'
asientoD='🟢'


escenarioo=np.empty([10,10], object)
while True:
    fun.limpiarpantalla()
    
    fun.titulo('   CREATIVOS.CL')
    print('''
    1) Comprar entradas
    2) Mostrar ubicaciones disponibles
    3) Ver listado de asistentes
    4) Mostrar ganacias totales
    5) Salir
    ''')
    opcion=int(input('Seleccione : '))
    while opcion>5 or opcion<0:
        fun.printr('Opcion invalida!!! Seleccione nuevamente')
        opcion=int(input('Seleccione 1-5 : '))
    if opcion==5:
        print('Salir')
        break
    elif opcion==1:
        print('Comprar Entradas')
        cantidad=int(input('Cantidad de entradas 1-3 : '))
        while cantidad<1 or cantidad>3:
            fun.printr('Cantidad invalida')
            print('Seleccione nuevamente')
            cantidad=int(input('Cantidad de entradas 1-3 : '))
        if cantidad>=1 and cantidad<=3:
            for h in range(cantidad):
                print(f'    Entrada N°{h+1}')
                print('''
                1) Platinum, $120.000. (Asientos del 1 al 20).
                2) Gold, $80.000. (Asientos del 21 al 50).
                3) Silver, $50.000. (Asientos del 51 al 100.).
                ''')
                entrada=int(input('Seleccione : '))
                while entrada<1 or entrada>3:
                    fun.printr('Entrada invalida seleccione nuevamente')
                    entrada=int(input('Seleccione 1-3 : '))
                if entrada==1:
                    print('Platinum')
                    cepla+=1
                    fun.escenario()
                    for i in range(10):
                        for j in range(10):
                                if escenarioo[i,j]==None:
                                    print(f'{asientoD}',end=' ')
                                else:
                                    print(f'{asientoO}',end=' ')
                        print(' ')
                    print(' ')
                    c=int(input('seleccione la fila 1-10 : '))
                    while c>10:
                        print('fila invalida,seleccione nuevamente')
                        c=int(input('sealeccione la fila 1-10 : '))
                    a=int(input('Seleccione columna 1-2 : '))
                    while a>2:
                        print('Fila invalida,seleccione nuevamente')
                        a=int(input('Seleccione columna 1-2 : '))
                    while c==asientoO and a==asientoO:
                        fun.printr('Asiento ocupado,seleccione nuevamente')
                        c=int(input('seleccione la fila 1-10 : '))
                        a=int(input('Seleccione columna 1-2 : '))
                    fun.printv('Asiento Comprado')
                    for i in range(10):
                        for j in range(10):
                            pass
                    fun.pausa()
                    rut=int(input('Ingrese su rit sin punto ni guion : '))
                    rut.append()
                    fun.pausa()
                        

                elif entrada==2:
                    print('Gold')
                    cegol+=1
                    fun.escenario()
                    for i in range(10):
                        for j in range(10):
                                if escenarioo[i,j]==None:
                                    print(f'{asientoD}',end=' ')
                                else:
                                    print(f'{asientoO}',end=' ')
                        print(' ')
                    print(' ')
                    asiento=int(input('Seleccione asiento 21-50 : '))
                    for i in range(10):
                        for j in range(10):
                            if asiento in escenarioo:
                                print(f'{asientoO}')
                                fun.pausa()
                    rut=int(input('Ingrese su rit sin punto ni guion : '))
                    rut.append()
                    fun.pausa()
                elif entrada==3:
                    print('silver') 
                    cesil+=1
                    fun.escenario()
                    for i in range(10):
                        for j in range(10):
                                if escenarioo[i,j]==None:
                                    print(f'{asientoD}',end=' ')
                                else:
                                    print(f'{asientoO}',end=' ')
                        print(' ')
                    print(' ')
                    asiento=int(input('Seleccione asiento 51-100 : '))
                    for i in range(10):
                        for j in range(10):
                            if asiento in escenarioo:
                                print(f'{asientoO}')
                                fun.pausa()
                    rut=int(input('Ingrese su rit sin punto ni guion : '))

                    fun.printv('Rut ingresado')
                    fun.pausa()
                
    elif opcion==2:
        print('Mostrar ubicaciones disponibles')
        print('Asientos disponibles')
        fun.escenario()
        for i in range(10):
            for j in range(10):
                    if None in escenarioo:
                        print(f'{asientoD}',end=' ')
                    else:
                        print(f'{asientoO}',end=' ')
            print(' ')
        print(' ')
        fun.pausa()
    elif opcion==3:
        print('Ver listado de asistentes')
        print(f'{rut}')
        fun.pausa()
    elif opcion==4:
        print('Mostrar ganacias totales')
        totalp=epla*cepla
        totalg=egol*cegol
        totals=esil*cesil
        print(f'''
     __________________________________________
    |    Tipo Entrada   |  Cantidad  |  Total  |
    |___________________|____________|_________|
    | Platinum {epla}   |{cepla}|   {totalp} |
    | Gold     {egol}    |{cegol}|  {totalg}  |
    | Silver   {esil}    |{cesil}|  {totals}  |
    |___________________|____________|_________|
    TOTAL {epla*cepla+egol*cegol+esil*cesil}
    ''')
        fun.pausa()



