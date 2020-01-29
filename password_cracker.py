#_.*_coding:Latin-1-*

##password_cracker written vy "Youc3f"

import hashlib
import sys



while True:
    try:
        wordlist_user = input('Entrez votre wordlist:')
        wordlist_user='E:\\Python\\Dev\\'+ wordlist_user
        wordlist=open(wordlist_user, 'r')
        print (wordlist_user)
        
        hash=input('entre ton hash sha224 : ')
        break
    except:
       print ('pas de fichier portant ce nom  \n')
    
for word in wordlist.readlines():
    word=word.strip('\n')

print (word)
wordlist_hash = hashlib.sha224(b"word").hexdigest()

print (wordlist_hash)    

if (hash ==wordlist_hash):
    print ('password FOUND ==>'+word )
else:
    print ('password not FOUND! ')
        
