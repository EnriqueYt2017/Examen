import numpy as np
import os
import time
import msvcrt
from colorama import Fore,Style,Back, init
init()
init(autoreset=True)
epla=120000
egol=80000
esil=50000

cepla=0
cegol=0
cesil=0

def pausa():
    printv('<<<Presione para continuar>>>')
    msvcrt.getch()
def printv(texto):
    print(f'{Fore.YELLOW}{texto}')

def limpiarpantalla():
    os.system("cls")
    printv('<<<Presione para continuar>>>')
    msvcrt.getch()
def tiempo():
    print('cargandooo.......')
    time.sleep(5)

def escenario():
    print('   ________________________________')
    print('  |           ESCENARIO            |')
    print('  |________________________________|')
    print(' 1   2   3   4   5   6   7   8   9  10')

def titulo(texto):
    print(' ____________________')
    print(f'|{Style.BRIGHT}{texto}     |')
    print('|____________________|')

def printr(texto):
    print(f'{Fore.RED}{Style.BRIGHT}{texto}')


