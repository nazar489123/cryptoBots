from lib2to3.pytree import convert
import time
import sys
import bit
from bit import Key

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
#gauth.LocalWebserverAuth() 
#gauth.SaveCredentialsFile("mycreds.txt")   
gauth.LoadCredentialsFile("mycreds.txt")    
drive = GoogleDrive(gauth) 

#profitfile = drive.CreateFile({'title': 'profit.txt'})
#profitfile.Upload()
file_list = drive.ListFile({'q': 'trashed=false'}).GetList()
file_id = file_list[0]['id'] # get the file ID

file = drive.CreateFile({'id': file_id})
file.GetContentFile('base.txt')

for file in file_list:
        if file['title']=='profit.txt':
                profitfile = drive.CreateFile({'id': file['id']})
                profitfile.GetContentFile('profit.txt')
        if file['title']=='base.txt':
                basefile = drive.CreateFile({'id': file['id']})
                basefile.GetContentFile('base.txt')

bytes_io = basefile.content
byte_str = bytes_io.read()
text_obj = byte_str.decode('UTF-8') 
f = list(text_obj.split('\n'))
def reloadBase():
        file_list = drive.ListFile({'q': 'trashed=false'}).GetList()
        file_id = file_list[0]['id'] # get the file ID

        file = drive.CreateFile({'id': file_id})
        file.GetContentFile('base.txt')

        for file in file_list:
                if file['title']=='profit.txt':
                        profitfile = drive.CreateFile({'id': file['id']})
                        profitfile.GetContentFile('profit.txt')
                if file['title']=='base.txt':
                        basefile = drive.CreateFile({'id': file['id']})
                        basefile.GetContentFile('base.txt')
        bytes_io = basefile.content
        byte_str = bytes_io.read()
        text_obj = byte_str.decode('UTF-8') 
        f = list(text_obj.split('\n'))
def addToProfitFile(intkey):
        content = profitfile.GetContentString()
        profitfile.SetContentString(content+intkey+"\n")
        profitfile.Upload()
        
def func(privhexdec):
        time.sleep(1)
        k = bit.PrivateKey.from_int( int(privhexdec))
        print('проверка кошелька', k.address)
        k.get_balance()
        print('Баланс:',k.balance)
        if k.balance > 0: 
                addToProfitFile(privhexdec)

while True:
        reloadBase()
        for elem in f: 
                if elem == ' ':
                        continue
                if elem == '':
                        continue
                func(elem)
        time.sleep(20)
