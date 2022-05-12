import socket, os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

allports = []
openlist = []
closedlist = []

class scanner:
    def port_scan():
        ip = input("[INPUT] Enter IP: ")

        print('-' * 50)

        ask_ports_amount = int(input("[*] Enter amount of ports to scan (Ex: 10, Will scan 1-10): "))

        for port in range(1, ask_ports_amount):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            check = sock.connect_ex((ip, port))

            allports.append(port)

            if check == 0:
                print(f"[+] Port {port} is open")
                openlist.append(port)
            else:
                print(f"[-] Port {port} is closed")
                closedlist.append(port)
            sock.close()

        print("-------------------------")
        print("[+] Open ports saved to open_ports.txt")
        with open("open_ports.txt", "w") as f:
            for port in openlist:
                f.write(str(port) + "\n")
        f.close()
        print("-------------------------")
        print("\n")

        print("-------------------------")
        print("[-] Closed ports saved to closed_ports.txt")
        with open("closed_ports.txt", "w") as f:
            for port in closedlist:
                f.write(str(port) + "\n")
        f.close()
        print("-------------------------")
        print("\n")
        ask_to_scan_port_info = input("[INPUT] Would you like to scan the ports to get info on the ports? Y/N: ")

        if ask_to_scan_port_info == 'Y' or ask_to_scan_port_info == 'y':
            scanner.port_info()
        else:
            pass

    def port_info():

        ports = []

        for port in allports:
            ports.append(port)

        print('-' * 50)
        print('Port Information Scanner')
        print('-' * 50)
        for port in ports:
            try:
                service = socket.getservbyport(int(port))
                print('[+] Port ' + str(port) + ' is {}'.format(service))
            except OSError:
                print(f'[-] Port {port} is not recognized.')
            
        print('-' * 50)


def main():
    clear()
    
    print("""
    ██████╗  ██████╗ ██████╗ ████████╗██╗███╗   ██╗███████╗ ██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝██╔═══██╗
    ██████╔╝██║   ██║██████╔╝   ██║   ██║██╔██╗ ██║█████╗  ██║   ██║
    ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██║██║╚██╗██║██╔══╝  ██║   ██║
    ██║     ╚██████╔╝██║  ██║   ██║   ██║██║ ╚████║██║     ╚██████╔╝
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                     https://github.com/iUseYahoo
    """)

    while True:
        print("1 - scan | Scan for ports on an IP\n2 - info | Get info on open and closed scanned ports")

        cmd = int(input("[INPUT] Enter a number> "))

        if cmd == 1:
            scanner.port_scan()
        elif cmd == 2:
            scanner.port_info()
        else:
            print("[ERROR] Invalid input")


if __name__ == '__main__':
    main()