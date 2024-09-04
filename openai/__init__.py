import sys, os, subprocess
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
    options = ["1","2","3","4","5","6","0"]
    while True:
        print( 
            "openAI capabilities\n\n"
            "1. Vision\n"
            "2. Text Generation\n"
            "3. Function Calling\n"
            "4. Structured JSON outputs\n"
            "5. Advanced Usage\n"
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
            elif option == "3":
                print("TO DO")
            elif option == "4":
                print("TO DO")
            elif option == "5":
                print("TO DO")
            elif option == "6":
                print("TO DO")
        else:
            print("Opcion no valida. Por favor, intenta nuevamente.")
        

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