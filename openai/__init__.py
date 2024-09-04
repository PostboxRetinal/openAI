import sys, os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import tests.text_generation as TG
import tests.vision as VI

def plataforma():
    '''
    Función para determinar la plataforma en la que se está ejecutando el script'''
    if os.name == 'nt':
        return 'windows'
    else:
        return 'linux'
    
def esperar():
    '''
    Función para esperar a que el usuario presione una tecla para continuar'''
    print()
    input("Presiona enter para continuar...")

def menu():
    '''
    Función para mostrar el menú principal'''
    options = ["1","2","0"]
    while True:
        print( 
            "openAI capabilities\n\n"
            "1. Text Generation\n"
            "2. Vision\n"
            "0. Salir\n\n"
        )

        option = input("Ingresa la opción: ")

        if option == "0":
            print("Hasta luego!")
            exit(0)
        elif option in options:
            if option == "1":
                print(TG.text_generation())
                esperar()
            elif option == "2":
                print(VI.vision())
                esperar()
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")
        

#Exec Menu

print(f"Binvenido al demo de openAI\nCorriendo desde {plataforma()}\n\n")

try:
    menu()

except KeyboardInterrupt:
    salida = input('\n*¿Desea salir del programa? S/N: * ').lower()
    if salida == 'n':
        print('\n Ok, no ha pasado nada ;) \n')
        menu()
    else:
        exit(0)