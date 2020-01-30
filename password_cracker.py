#_.*_coding:Latin-1-*

##password_cracker written vy "Youc3f"

import hashlib


while True:
    try:
        wordlist_user = input('Entrez votre wordlist:')
        wordlist_user='E:\\Python\\Dev\\'+ wordlist_user+'.txt'
        print ("Fichier : "+wordlist_user)
        
        wordlist=open(wordlist_user, 'w+')
        
        password=input('entre ton password : ')
        break
    except:
       print ('pas de fichier portant ce nom  \n')
    
wordlist_hash = hashlib.sha224(b"password").hexdigest()

print (password, wordlist_hash)   

wordlist.write(password+' '+wordlist_hash)
wordlist.close()
exit;


#for word in wordlist.readlines():
#    word=word.strip('\n')
#
#
#if (hash ==wordlist_hash):
#    print ('password FOUND ==>'+word )
#else:
#    print ('password not FOUND! ')
#
