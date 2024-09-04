import sys, os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import tests.text_generation as TG
import tests.vision as VI


def menu():
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
            elif option == "2":
                print(VI.vision())
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
try:
    menu()
except KeyboardInterrupt:
    salida = input('\n*¿Desea salir del programa? S/N: * ').lower()
    if salida == 'n':
        print('\n Ok, no ha pasado nada ;) \n')
        menu()
    else:
        exit(0)