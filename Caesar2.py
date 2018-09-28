txt = 'MEBCO ZYWZOI KXN RSC VOQSYXZ OFOBIYXO PKVV LKMU DY ZRKBCKVEC'

while True:
    def decode():
        shift = input('Shift number: ')
        for i in txt:
            msg = (ord(i) - int(shift))
            if msg == 32 - int(shift):
                msg = msg + int(shift)
            elif msg < 65:
                msg = msg + 26
            
            print(chr(msg))
 
 
    print('')
    decode()
