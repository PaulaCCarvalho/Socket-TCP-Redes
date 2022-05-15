
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



serverPort = 8888
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(10)
print('O servidor está pronto para receber...')

while True: 
    connectionSocket, clientAdress = serverSocket.accept()
    conteudo = connectionSocket.recv(1024)
    
    CHAVE = unpack(">150si", conteudo)[1]
    mensagem = unpack('>150si', conteudo)[0].decode()

    descriptografar = descriptografia(mensagem, CHAVE)
    print("From cliente: " + descriptografar) 

    criptografar = criptografia(descriptografar, CHAVE)
    connectionSocket.send(pack('>150si', criptografar.encode(), CHAVE))

    connectionSocket.close()