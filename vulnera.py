import tkinter as tk
import nmap
import socket

def get_local_ip():
    try:
        # Créez une connexion de test avec une adresse IP externe
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return ""

def scan_vulnerabilities():
    target = entry.get()  # Récupère l'adresse IP saisie dans le champ de saisie

    if not target:
        target = get_local_ip()

    if target:
        scanner = nmap.PortScanner()
        scanner.scan(target, '1-1000', '-sV -Pn -O')

        for host in scanner.all_hosts():
            if scanner[host].state() == 'up':
                print(f"Host: {host}")

                for proto in scanner[host].all_protocols():
                    ports = scanner[host][proto].keys()

                    for port in ports:
                        service = scanner[host][proto][port]
                        print(f"Port: {port}\tService: {service['name']}\tState: {service['state']}\tVersion: {service['version']}")
    else:
        print("Adresse IP non valide")

# Création de l'interface utilisateur
window = tk.Tk()
window.title("Analyse de vulnérabilités")
window.geometry("300x200")

label = tk.Label(window, text="Entrez l'adresse IP à analyser (ou laisser vide pour utiliser l'adresse IP locale) :")
label.pack(pady=10)

entry = tk.Entry(window, width=20)
entry.pack(pady=5)

button = tk.Button(window, text="Analyser", command=scan_vulnerabilities)
button.pack(pady=10)

window.mainloop()
