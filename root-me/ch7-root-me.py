#python2
with open('ch7.bin') as f:
    cipher = f.read()

for x in range(256):
    print(''.join([chr((ord(y) + x) % 256) for y in cipher]))
