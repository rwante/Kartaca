import base64
import os

dosya_path = "C:/Users/user/Desktop/Kartaca/"
dosyalar = os.listdir(dosya_path)
liste = []
for dos in dosyalar:
    base64_bytes = dos.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    liste.append([int(message),dos])
liste.sort()
print(liste)
binary_int = int("11000010110001001100011", 2)
byte_number = binary_int.bit_length()
for i in range(0,492):
    dosya_open = open(dosya_path+"/"+liste[i][1],"r")
    text = dosya_open.readline()
    print(text)
    dosya_open.close()
