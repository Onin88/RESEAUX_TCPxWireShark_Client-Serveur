from socket import *
import sys


try:
    server_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
except error as e:
    print(f"Erreur lors de la création du socket : {e}")
    sys.exit(-1)


try:
    server_socket.bind(('', 1234))
except server_socket.error as e:
    print(f"Erreur lors de la liaison du socket : {e}")
    server_socket.close()
    exit()

server_socket.listen(1)

try:
    (socket2, adresse_client) = server_socket.accept()
except socket.error as e:
    print(f"Erreur lors de l'acceptation de la connexion : {e}")
    server_socket.close()
    exit()


# Réception
try:
    message_bytes = socket2.recv(60)
except ValueError as e:
    print(f"Erreur lors de la récéption : {e}")
    socket2.close()
    server_socket.close()
    exit()
except timeout:
    print("Le temps d'attente est écoulé sans recevoir de données.")
    socket2.close()
    server_socket.close()
    exit()

message = str(message_bytes, "utf-8")
message_bytes = bytes(message.upper(), "utf-8")

# Envoi
try:
    sent = socket2.send(message_bytes)
except ValueError:
    print("Erreur lors de l'envoi")
    socket2.close()
    server_socket.close()
    exit()
except IndexError:
    print("Erreur dans l'ip ou le port")
    socket2.close()
    server_socket.close()
    exit()
except:
    print("Une erreur inattendue s'est produite lors de l'envoi")
    socket2.close()
    server_socket.close()
    exit()

print(f"Message reçu de {adresse_client[0]}:{adresse_client[1]}")

socket2.close()
server_socket.close()