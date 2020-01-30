#_.*_coding:Latin-1-*

import socket
import subprocess
import sys
from datetime import datetime


#subprocess.Popen(   ['cls' ] )                  #Nettoyer le terminal
remote_server=input('entrer le nom de domaine :')
remove_server_IP=socket.gethostbyname(remote_server)

print ('IPv4:', remove_server_IP)               #afficher l'adresse IPV4 de la cible
print ("-"*60)

print ('please wait while scanning', remove_server_IP)
t1=datetime.now()

try:
    for port in range(1, 85):
        connexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultat=connexion.connect_ex((remove_server_IP, port))
        if resultat== 0:                            #si aucune erreur n'est rencontrée
            print ('port {}:open'.format(port))
        else:
            print ('port {}:closed'.format(port))    
            connexion.close()       #clore la connexion
except KeyboardInterrupt :
    print ('you pressed CtrlC')
    sys.exit()                              #arreter l'execution du script  
    
except :
    print ('something wrong !!')
    sys.exit()
        
t2=datetime.now()
Total =t2-t1
print ('-'*60)
print ('scan done in', Total, 'second')            #afficher le temps total du scanning

