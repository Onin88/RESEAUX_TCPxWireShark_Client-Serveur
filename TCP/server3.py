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
clients = {}

while True:
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

    # On identifie le client par son adresse IP et son port
    client_addr = (adresse_client[0], adresse_client[1])

    # On complete la liste des nombres associés à ce client
    if client_addr not in clients:
        clients[client_addr] = []
    clients[client_addr].append(int.from_bytes(message_bytes[:4], byteorder="big"))

    # Si le client a envoyé deux nombres, alors on les additionne et on renvoi le résultat au client
    if len(clients[client_addr]) == 2:
        nombre1, nombre2 = clients[client_addr]
        nombre = nombre1 + nombre2
        message_bytes = nombre.to_bytes(4, byteorder="big")

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

        # On réinitialise la liste des nombres associés au client
        clients[client_addr] = []