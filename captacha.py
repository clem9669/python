import websocket
# https://lab.algonics.net/anticaptcha
url = 'ws://lab.algonics.net/anticaptcha/ws'
ciphertext = "e:hz hsciavy rwx rjyt eaamgigs wqmegfaix fum xejvuwfinswyzawmldlk. fjgg fjyf" #76 long
# previsionPlainText = "le/ce message/drapeau est XXX. bien joue" ==> unnecessary oracle
ws = websocket.WebSocket()
ws.connect(url)

print(">", ws.recv()) #"coucou!"
input="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" #null in vernam
while True:
    a=ws.send('{"message": "'+input+'"}') # "A"*30
    chall = ws.recv()
    #print(">",chall) # {"challenge":"1a47c37ac4a42"}
    base=chall[14:]
    fin= ''.join( c for c in base if  c not in '}()""{' ) #remove undesirable characters
    numero=int(fin, 13) #convert base13 to base10
    response = '{"reponse":'+str(numero)+'}'
    ws.send(response)
    voila=ws.recv()
    print(">",voila)
    if voila[15]=='e':
        print(">>>",voila) ##e:wvebctwvebctwvebctwvebctwvebctwvebctwvebctwvebctwve: repeat 6 char
        ws.close()
        break

#key
print(">>> [key looping after 6 char]")
key=voila[17:23]
print(">>> key = ", key)

#converting ciphertext to claintext with key found
cipheronlyText = ciphertext[2:].replace(" ","").replace(".","")
print(">>> Cipher:", cipheronlyText)
keyAdjusted = (key*13)[0:len(cipheronlyText)]
print(">>> Key:   ", keyAdjusted)


#decrypt by reducing to a=0 & z=25
i=0
plaintext=""
while i<len(cipheronlyText):
    plaintext = plaintext + chr((ord(cipheronlyText[i]) - ord(keyAdjusted[i]))%26+ord('a'))
    i = i + 1
print(plaintext)
