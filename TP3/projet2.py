import socket
import matplotlib.pyplot as plt


# Fonction pour scanner un port
def scanner_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout pour éviter les longs blocages
            result = s.connect_ex((ip, port))  # 0 si le port est ouvert
            if result == 0:
                print(f"Port {port} ouvert sur {ip}")
                return True
            else:
                return False
    except Exception as e:
        print(f"Erreur lors de la vérification du port {port} : {e}")
        return False

def scanner_ports(ip, ports):
    print(f"Scan en cours pour l'adresse IP : {ip}")
    for port in ports:
        scanner_port(ip, port)


def visualiser_ports(ip, ports):
    ouverts = []
    fermes = []

    for port in ports:
        if scanner_port(ip, port):
            ouverts.append(port)
        else:
            fermes.append(port)

    # Graphique
    plt.bar(["Ouverts", "Fermés"], [len(ouverts), len(fermes)], color=["green", "red"])
    plt.title(f"Résultat du scan de ports pour {ip}")
    plt.ylabel("Nombre de ports")
    plt.show()


if __name__ == "__main__":
    ip_cible = input("entrer une adresse ip. voici un exemple: 127.0.0.1 ")
    ports_a_tester = [22, 80, 443, 8080]
    scanner_ports(ip_cible, ports_a_tester)
    visualiser_ports(ip_cible, ports_a_tester)