import random
import socket
import os
import webbrowser
import requests
import json

from colorama import Fore
from colorama import Style

clear = lambda: os.system('cls')
clear()

print(f'''{Fore.RED}

         ██████╗ █████╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
        ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
        ██║     ███████║██████╔╝██╔██╗ ██║███████║██║  ███╗█████╗  
        ██║     ██╔══██║██╔══██╗██║╚██╗██║██╔══██║██║   ██║██╔══╝  
        ╚██████╗██║  ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      

                        | Creado por TeoUwUxd |

        
        [ 1 ] Generar ipv4 Falsa
        [ 2 ] IPLoggers
        [ 3 ] Geolocalizar IP
        [ 99 ] Cerrar la terminal

''')

opcion = int(input("  [~] Elije una opción: "))

def FALSA_IP():
    print("")

    gen_ip_num = int(input("  [~] Cuántas ipv4 falsas quieres generar?: "))
    print("")

    def main():
        
        ip = "192.168."
        ip += ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(2))))
                        
        print(f"{Fore.GREEN}  [+] ipv4 falsa generada correctamente: {Style.RESET_ALL}" + ip)
        print("")

    try:
        for i in range(gen_ip_num):
            if __name__ == '__main__':
                main()

    except:
        print(f"{Fore.RED}  [-] No se han podido generar las ipv4 falsas! {Style.RESET_ALL}")
        print("")

def IPLOGGER():
    clear()
    print(f'''{Fore.RED}

         ██████╗ █████╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
        ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
        ██║     ███████║██████╔╝██╔██╗ ██║███████║██║  ███╗█████╗  
        ██║     ██╔══██║██╔══██╗██║╚██╗██║██╔══██║██║   ██║██╔══╝  
        ╚██████╗██║  ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  

                        | Creado por TeoUwUxd |


        [ 1 ] IPLogger.org
        [ 2 ] Grabify
        [ 99 ] Salir

    ''')

    opcionIPL = int(input("  [~] Elije una opción: "))

    def IPLogger():
        try:
            url = ['https://iplogger.org/']

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

            h = webbrowser.get('chrome')
            h.open(url[0])

            print(f"{Fore.GREEN}  [+] La página web se ha podido abrir correctamente! {Style.RESET_ALL}")
        
        except:
            print(f"{Fore.RED}  [-] Ha ocurrido un error y no se ha podido abrir la página web correctamente! {Style.RESET_ALL}")
            print("")

    def Grabify():
        try:
            url = ['https://grabify.link/']

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

            h = webbrowser.get('chrome')
            h.open(url[0])

            print(f"{Fore.GREEN}  [+] La página web se ha podido abrir correctamente! {Style.RESET_ALL}")

        except:
            print(f"{Fore.RED}  [-] Ha ocurrido un error y no se ha podido abrir la página web correctamente! {Style.RESET_ALL}")
            print("")

    
    if opcionIPL == 1:
        IPLogger()
    
    elif opcionIPL == 2:
        Grabify()

    elif opcionIPL == 99:
        exit()
        print(f"{Style.RESET_ALL}")

def GEOIP():
    clear()
    print(f'''{Fore.RED}

         ██████╗ █████╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
        ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
        ██║     ███████║██████╔╝██╔██╗ ██║███████║██║  ███╗█████╗  
        ██║     ██╔══██║██╔══██╗██║╚██╗██║██╔══██║██║   ██║██╔══╝  
        ╚██████╗██║  ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  

                        | Creado por TeoUwUxd |


        [ 1 ] Geolocalizar IP
        [ 2 ] Reverse DNS IP
        [ 99 ] Salir

    ''')

    opcionGIP = int(input("  [~] Elije una opción: "))

    if opcionGIP == 1:

        print("")
        ipgip = str(input(f"  [~] IP: {Style.RESET_ALL}"))
        try:
            request_url = 'https://geolocation-db.com/jsonp/' + ipgip
            response = requests.get(request_url)
            result = response.content.decode()

            result = result.split("(")[1].strip(")")

            result  = json.loads(result)
            print("")
            print("  " + result)
            print("")
            print(f"{Fore.GREEN}  [+] La información se ha conseguido correctamente!{Style.RESET_ALL}")

        except:
            print("")
            print(f"{Fore.RED}  [-] La información no se ha conseguido correctamente!{Style.RESET_ALL}")

    if opcionGIP == 2:

        print("")
        ipgipdns = str(input("  [~] IP: "))
        try:
            domain_name = socket.gethostbyaddr(ipgipdns)[0]

            print("  " + domain_name)
            print("")
            print(f"{Fore.GREEN}  [+] Reverse DNS IP conseguida correctamente! {Style.RESET_ALL}")

        except:
            print(f"{Fore.RED}  [-] No se ha podido conseguir la Reverse DNS IP correctamente! {Style.RESET_ALL}")

    if opcionGIP == 99:
        print(f"{Style.RESET_ALL}")
        exit()


if opcion == 1:
    FALSA_IP()

elif opcion == 2:
    IPLOGGER()

elif opcion == 3:
    GEOIP()

elif opcion == 99:
    exit()
    print(f"{Style.RESET_ALL}")
