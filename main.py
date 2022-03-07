import time
import paramiko
from getpass import getpass
from colorama import Fore, init
init()

print(Fore.RED + "----------------- Infohard LEMA -----------------")

# Credenciales
HOST = input("Introduce tu dirección IP: ")
USER = input("Introduce el nombre del usuari del host: ")

if __name__ == '__main__':
    try:
        # Conexión con el equipo por SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )

        # Contraseña del usuari
        password = getpass('Ingrese su contraseña: ')

        client.connect(HOST, username=USER, password=password)

        while True:
            # Menú principal
            print("************************************************************************************************************************")
            print("""************************************************************************************************************************""")  
            opcion = int(input("""Elige opción: 
            \n 
            · General Info   [1]           · Info Memory       [2] \n 
            · Info CPU       [3]           · Info Network      [4] \n 
            · Info Processes [5]           · Salir             [6]
            \n > """))

            if opcion == 1:
                stdin, stdout, stderr = client.exec_command('lshw -short')

                time.sleep(1)

                result = stdout.read().decode()

                print(result)
        
            elif opcion == 2:
                stdin, stdout, stderr = client.exec_command('free')

                time.sleep(1)

                result = stdout.read().decode()

                print(result)
            
            elif opcion == 3:
                stdin, stdout, stderr = client.exec_command('cat /proc/cpuinfo')

                time.sleep(1)

                result = stdout.read().decode()

                print(result)

            elif opcion == 4:
                stdin, stdout, stderr = client.exec_command('ip a')

                time.sleep(1)

                result = stdout.read().decode()

                print(result)
            
            elif opcion == 5:
                stdin, stdout, stderr = client.exec_command('ps -l')

                time.sleep(1)

                result = stdout.read().decode()

                print(result)
            
            elif opcion == 6:
                break

            else:
                print("Lo siento esa opcion no està contemplada.")

    except paramiko.ssh_exception.AuthenticationException as e:
            print('Autenticación fallida')
        
    except:
        print("ERROR!")
   

        
