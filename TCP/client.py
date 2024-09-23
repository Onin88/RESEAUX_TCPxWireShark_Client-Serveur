from socket import *
import sys
# Reset le port : sudo iptables -A INPUT -p tcp -i eth0 --dport 1234 -j DROP

if len(sys.argv) != 3:
    print("Veuillez spécifier l'adresse IP et le port du serveur en argument <ip> <port>")
    sys.exit(-1)

host = sys.argv[1]
port = int(sys.argv[2])

try:
    mysocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
except error as e:
    print(f"Erreur lors de la création du socket : {e}")
    sys.exit(-1)

message = "J'aime le cours de Réseaux 2"
message_bytes = bytes(message, "utf-8")

try:
    mysocket.connect((host, port))
except error as e:
    print(f"Erreur lors de la connexion au serveur : {e}")
    mysocket.close()
    sys.exit(-1)

try:
    sent = mysocket.send(message_bytes)
except error as e:
    print(f"Erreur lors de l'envoi du message : {e}")
    mysocket.close()
    sys.exit(-1)

try:
    resultat_bytes = mysocket.recv(60)
except error as e:
    print(f"Erreur lors de la réception du message : {e}")
    mysocket.close()
    sys.exit(-1)

resultat = str(resultat_bytes, "utf-8")
print(resultat)

mysocket.close()
