from socket import *
import sys

if len(sys.argv) != 3:
    print("Veuillez spécifier l'adresse IP et le port du serveur en argument <ip> <port>")
    sys.exit(-1)

host = sys.argv[1]
port = int(sys.argv[2])

try:
    client_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
except error as e:
    print(f"Erreur lors de la création du socket : {e}")
    sys.exit(-1)

try:
    client_socket.connect((host, port))
except error as e:
    print(f"Erreur lors de la connexion au serveur : {e}")
    client_socket.close()
    sys.exit(-1)

input1 = [0, 0]

for i in range(2):
    try:
        input1[i] = int(input("Donner un entier : "))
    except ValueError:
        print("Veuillez entrer des entiers")
        client_socket.close()
        sys.exit()

    nombre = input1[i].to_bytes(4, byteorder="big")

    # Envoi
    try:
        sent = client_socket.send(nombre)
    except error as e:
        print(f"Erreur lors de l'envoi du message : {e}")
        client_socket.close()
        sys.exit(-1)


# Réception
try:
    resultat_bytes = client_socket.recv(60)
except error as e:
    print(f"Erreur lors de la réception du message : {e}")
    client_socket.close()
    sys.exit(-1)

nombre = int.from_bytes(resultat_bytes[:4], byteorder="big")
print(f"Voila le résultat de {input1[0]} + {input1[1]} : {nombre}")

client_socket.close()
