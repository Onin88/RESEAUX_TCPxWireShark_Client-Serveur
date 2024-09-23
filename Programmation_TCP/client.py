# Description: Client TCP - Programmation TCP/IPv6
from socket import *
from select import *
import sys

#Ex1###########################
def send_whole(S, T):
    envoye = 0
    while envoye < len(T):
        envoye += S.send(T[envoye:].encode("utf-8"))
################################


#Ex2######################################################
try:
    mysocket = socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP)
    mysocket.connect(("::1", 7777))
except error as e:
    print(f"Erreur socket : {e}")
    sys.exit(-1)


message = "A" * 50000
message_bytes = bytes(message, "utf-8")
try:
    send_whole(mysocket, message)
    print(f"Message envoyé : {message}")
    mysocket.close()
except error as e:
    print(f"Erreur envoie message : {e}")
    mysocket.close()
    sys.exit(-1)
############################################################