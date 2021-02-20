# -*- coding: utf-8 -*-
"""
"""

import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
import os
import json

def generateKey(pswd):
    password = pswd.encode()  
    salt = b'\x94+\x19\x0bF1\x10\xe0\xe0#\x16\xcd\x7f\x86pg'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  
    return key

def encryption(key, filename):
    input_file = filename+".json"
    output_file = filename+'.encrypted'
    
    with open(input_file, 'rb') as f:
        data = f.read()  
    
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    
    with open(output_file, 'wb') as f:
        f.write(encrypted)  

#El metodo recibe una lista de diccionarios o JSONs
#Si esta vacía, crea el archivo JSON
#Si no esta vacia, solo cifra 
def encryptionJSON(key, lista):
    output_file = 'db.encrypted'
    input_file = "db.json"
    
    if len(lista)==0:
        output_file = 'db.json'
        with open(output_file, 'wb') as f:
            pass
    else: 
        #jsonStr = json.dumps(lista)
        with open(input_file, "w") as outfile:  
            json.dump(lista, outfile)
        with open(input_file, 'rb') as f:
            data=f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(encrypted)  
        removeFile("db.json")
    
def decryptionJSON(key):
    input_file = 'db.encrypted'
    output_file = "db.json"
    
    try:
        with open(input_file, 'rb') as f:
            data = f.read()  
        fernet = Fernet(key)
        try:
            decrypted = fernet.decrypt(data)
            s=str(decrypted,'utf-8')
            lst=json.loads(s)
            jsonStr=json.dumps(lst)
            return jsonStr
        except InvalidToken:
            print("Invalid Key - Unsuccessfully decrypted")
    except FileNotFoundError:
        jsonStr=None
        return jsonStr

def decryption(key, filename):
    input_file = filename+'.encrypted'
    output_file = filename+".json"
    try:
        with open(input_file, 'rb') as f:
            data = f.read()  
            
        fernet = Fernet(key)
        try:
            decrypted = fernet.decrypt(data)
            """
            s=str(decrypted,'utf-8')
            data = StringIO(s) 
            df=pd.read_csv(data)
            return df
            """
            with open(output_file, 'wb') as f:
                f.write(decrypted)  # Write the decrypted bytes to the output file
        
        except InvalidToken:
            print("Invalid Key - Unsuccessfully decrypted")
    except FileNotFoundError:
         return 0

def saveKey(key):
    with open("key.key", "wb") as key_file:
            key_file.write(key)
def removeFile(filename):
    os.remove(filename)

####################################################
lista=[{
    "Usuario": "Miguel Gonzalez",
    "Correo": "m.gonzi@hotmail.com",
    "Facebook": "migue123",
    "Instagram": "Miguel321",
    "Banco": 2563
  },
  {
    "Usuario": "Juan Dominguez",
    "Correo": "j.domin@gmail.com",
    "Facebook": "juanito2000",
    "Instagram": "Juanito2012",
    "Banco": 4125
  }
]
lista2=[]

"""
#encriptar archivo
pswd="flandelaAbuelaenDomingo"
key=generateKey(pswd)
saveKey(key)
encryptionJSON(key,lista)
"""

pswdUsuario="flanlaAbuelaenDomingo"
keyUsuario=generateKey(pswdUsuario)
jsonStr=decryptionJSON(keyUsuario)
objJson=json.loads(jsonStr)
print(type(objJson))



