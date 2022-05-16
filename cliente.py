import sys

from socket import *
from struct import * 


def criptografia(mensagem, CHAVE):
    encriptada = []

    for caractere in mensagem:
        caractereASCII = ord(caractere)

        if caractereASCII >= 97 and caractereASCII <= 122:
            if ((caractereASCII + CHAVE) > 97) and ((caractereASCII + CHAVE) <= 122):
                encriptada.append(chr(caractereASCII + CHAVE))
            elif (caractereASCII + CHAVE) > 122:
                encriptada.append(chr((caractereASCII + CHAVE) - 26))
        else:
            print("ERROR AO CRIPTOGRAFAR SUA MENSAGEM\n >> Observação: Sua mensagem deve conter apenas letra minúsculas!")
            exit(1)
         
    return ''.join(encriptada)

def descriptografia(mensagem, CHAVE):
    descriptada = []

    for caractere in mensagem:
        caractereASCII = (ord(caractere) - CHAVE)
        if caractereASCII >= 97 and caractereASCII <= 122:
                descriptada.append(chr(caractereASCII))
        elif caractereASCII < 0:
                pass
        elif (caractereASCII) < 97:
                descriptada.append(chr(caractereASCII + 26))  
        else:
            print("ERROR AO DESCRIPTOGRAFAR SUA MENSAGEM\n >> Observação: Sua mensagem deve conter apenas letra minúsculas!")
            exit(1)
         
    return ''.join(descriptada)

def main(args):
    serverName = args[1]
    serverPort = int(args[2])
    mensagem = args[3]
    CHAVE = int(args[4])
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    
    string = criptografia(mensagem, CHAVE)
    clientSocket.send(pack('>150si', string.encode(), CHAVE))

    clientSocket.settimeout(15.0)
    conteudo = clientSocket.recv(1024)

    CHAVE = unpack(">150si", conteudo)[1]
    mensagem = unpack('>150si', conteudo)[0].decode()


    descriptografar = descriptografia(mensagem, CHAVE)
    print('From server: ', descriptografar)  
    clientSocket.close()
    

if __name__ == '__main__':
    sys.exit(main(sys.argv))