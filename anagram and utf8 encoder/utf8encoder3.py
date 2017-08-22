from sys import argv

path = argv[1]

fileout = open( "utf8encoder_out.txt", "wb")

with open(path, "rb") as f:
    byte = f.read(2)
    while byte != b"":
        s1 = hex(byte[0])[2:].zfill(2)
        s2 = hex(byte[1])[2:].zfill(2)
        s = s1+s2
        b = bin(int(s, 16))
        if int('0000',16) <= int(s,16) <= int('007F',16):
            a = b[2:].zfill(8)
            n1 = int(a,2)
            data1 = bytes([n1])
            fileout.write(data1)
        if int('0080',16) <= int(s1+s2,16) <= int('07FF',16):
            a = b[2:].zfill(11)
            n1 = int('110'+a[0:5],2)
            n2 = int('10'+a[5:],2)
            data1 =bytes([n1])
            data2 =bytes([n2])
            data = data1 + data2
            fileout.write(data1 +data2)
        if int('0800',16) <= int(s1+s2,16) <= int('FFFF',16):
            a= b[2:].zfill(16)
            n1 = int('1110'+a[0:4],2)
            n2 = int('10'+a[4:10],2)
            n3 = int('10'+a[10:],2)
            data1 =bytes([n1])
            data2 =bytes([n2])
            data3 =bytes([n3])
            data=data1+data2+data3
            fileout.write(data)
        byte = f.read(2)
fileout.close()