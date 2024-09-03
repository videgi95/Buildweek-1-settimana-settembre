import socket as so
from prettytable import PrettyTable

target_ip = input("Inserire l'ip del web server interessato: ")
portrange = input("Inserisci un port range (es 5-200): ")
lowport = 1
highport = 1024
if "-" in portrange:
    lowport = int(portrange.split('-')[0])
    highport = int(portrange.split('-')[1])

porte_aperte = []
porte_chiuse = []

# Scansione delle porte
def verificaSocket(ip, lowport, highport):
    for port in range(lowport, highport+1):
        s = so.socket(so.AF_INET, so.SOCK_STREAM)# utilizzo di AF_INET per connessione iPv4 e SOCK_STREAM per definire che il socket sia di tipo TCP
        so.setdefaulttimeout(0.1)  # Timeout di chiusura di connessione per non lasciare il programma in attesa di risposta troppo a lungo
        result = s.connect_ex((ip, port))  # Test di connessione alla porta(ritorna un errore e non alza l'eccezione in caso di errore)
        if result == 0: # connect_ex ritorna 0 in caso di connessione riuscita altrimenti qualsiasi altro errore risulta in porta chiusa
            #print(f"Porta {port}: Aperta")
            porte_aperte.append(port)
        else:
            porte_chiuse.append(port)
        s.close()
    return porte_aperte,porte_chiuse

def crea_tabella(target_ip , porte_aperte, porte_chiuse):
    count_aperte = 0
    count_chiuse = 0
    tabella1 = PrettyTable(['Porta','Stato'])
    tabella2 = PrettyTable(['Porta','Stato'])

    for port in porte_aperte:
        count_aperte = count_aperte + 1
        tabella1.add_row([port , 'Aperta'])

    for port in porte_chiuse:
        count_chiuse = count_chiuse + 1
        tabella2.add_row([port , 'Chiusa'])

    print(f"Risultati per la scansione su {target_ip}: \n\nTrovate {count_aperte} Porte aperte e {count_chiuse} Porte chiuse\n")
    print(tabella1)
    print(tabella2)


verificaSocket(target_ip, lowport, highport)
crea_tabella(target_ip , porte_aperte , porte_chiuse)
