txt = 'RXU UHLQIRUFHPHQWV ZLOO EH GHODBHG XQWLO QHAW ZHHN OHW XV KRSH WKH HQHPB GRHV QRW DWWDFN QRZ'
msg = []
decoded = []
for i in txt:
    msg.append(ord(i)-3)

for i in range(0, len(msg)):
    if msg[i] == 29:
        msg[i] = msg[i] + 3
    elif msg[i] < 65:
        msg[i] = msg[i] + 26

for i in msg:
    decoded.append(chr(msg[i]))
    
print(decoded)