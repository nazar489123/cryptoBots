import time
import sys
import bit
from bit import Key
from threading import Thread

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
#gauth.LocalWebserverAuth() 
#gauth.SaveCredentialsFile("mycreds.txt")   
gauth.LoadCredentialsFile("mycreds.txt")    
drive = GoogleDrive(gauth) 

#file = drive.CreateFile({'title': 'base.txt'})
#file.Upload()

file_list = drive.ListFile({'q': 'trashed=false'}).GetList()
file_id = file_list[0]['id'] # get the file ID
file = drive.CreateFile({'id': file_id})
file.GetContentFile('base.txt')
def addToBase(intkey):
        content = file.GetContentString()
        file.SetContentString(content+str(intkey)+"\n")
        file.Upload()
y=5000
def func():
        k = bit.PrivateKey.from_int(y)
        k.get_transactions()
        print('проверка:'+str(y))
        if len(k.transactions) > 0: 
                        addToBase(y)
                        print('что-то нашли ...'+k.address)
                        k.get_balance()
                        print('Баланс:',k.balance)
while True:
        func()
        y=y+1
