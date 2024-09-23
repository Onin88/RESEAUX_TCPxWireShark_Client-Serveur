from socket import *
from select import *
import sys



#Ex3#########################################
def recv_whole(S, L):
    nbAppel = 0
    message_bytes = b""
    while len(message_bytes) < L:
        msg = S.recv(L-len(message_bytes))
        message_bytes += msg
        if len(message_bytes) == 0:
            return (b"", 0)
        # nombre d'appel à recv
        nbAppel += 1
    return message_bytes, nbAppel
##############################################

num_client = 0

prises = {}
evenements = sum([POLLIN, POLLPRI, POLLERR, POLLHUP])

sondage = poll()

try:
    mysocket = socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP)
    mysocket.bind(("::1", 7777))
    mysocket.listen(32)

    numSocket = mysocket.fileno()
    prises[numSocket] = mysocket
    sondage.register(mysocket, evenements)

except error as e:
    print(f"Erreur socket : {e}")
    sys.exit(-1)


#Ex4#########################################
while True:

    try:
        num_actif = sondage.poll()[0][0]
        socket_actif = prises[num_actif]

        if num_actif == numSocket:
            (client, _) = socket_actif.accept()

            numClient = client.fileno()
            prises[numClient] = client
            sondage.register(client, evenements)
        else:
            (message, nbAppel) = recv_whole(socket_actif, 50000)
            print(f"Nombre d'appel à recv : {nbAppel}")
            print(f"Client numero : {num_client}")

            #Client déconnecté
            if(len(message) == 0):
                num_client += 1
                del prises[num_actif]
                sondage.unregister(socket_actif)
                socket_actif.close()

    except error as e:
        print(f"Erreur réception message : {e}")
        client.close()
        mysocket.close()
        sys.exit(-1)
##############################################