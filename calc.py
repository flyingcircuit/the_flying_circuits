txt = 'RXU UHLQIRUFHPHQWV ZLOO EH GHODBHG XQWLO QHAW ZHHN OHW XV KRSH WKH HQHPB GRHV QRW DWWDFN QRZ'


for i in txt:
    msg = (ord(i) - 3)
    if msg == 29:
        msg = msg + 3
    elif msg < 65:
        msg = msg + 26
    
    msg.append(ord(i)-3)
    
    print(chr(msg))
        