import socket as so

target_ip = "?????"#Inserire appena possibile l'ip del webserver di cisco packet tracer
portrange = input("Inserisci un port range (es 5-200): ")
lowport = 5
highport = 200
if "-" in portrange:
    lowport = int(portrange.split('-')[0])
    highport = int(portrange.split('-')[1])

# Scansione delle porte
def port_scan(ip, lowport, highport):
    for port in range(lowport, highport+1):
        s = so.socket(so.AF_INET, so.SOCK_STREAM)#utilizzo di AF_INET per connessione iPv4 e SOCK_STREAM per definire che il socket sia di tipo TCP
        so.setdefaulttimeout(1)  # Timeout di 1 secondo
        result = s.connect_ex((ip, port))  # Test di connessione alla porta
        if result == 0:
            print(f"Porta {port}: Aperta")
        else:
            print(f"Porta {port}: Chiusa")
        s.close()

port_scan(target_ip, lowport, highport)
