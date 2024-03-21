import re
while True:
    print("\n\nEnter dff value ")

    a = input()

    a = a.replace(" ","")
    b= re.findall(r"..",a)
    
    print("\n"+str(b))
    b.reverse()

    allStr = ""
    currentIndex = 0
    allStrList = [str]
    for item in b:
        binaryStr =  str(bin(int(item, base=16)))
        binaryWithout0b:str = binaryStr.split("b")[1]
        #print(binaryWithout0b)
        newStr = ""

        lengt = binaryWithout0b.__len__()
        for i in range(0,8-lengt):
            newStr+="0"
        binaryWithout0b = newStr+binaryWithout0b

        #print("Final binaryWithout0b =",binaryWithout0b)

        #print("Length "+str(lengt))
        dffBit = binaryWithout0b[0]
        #print(dffBit)
        binaryWithoutDFF:str = binaryWithout0b[1:9:1]
        #print(binaryWithoutDFF+"\n\n")
        allStr= allStr+ binaryWithoutDFF
    print("bin 0b"+allStr)
    print("dec 0d"+str(int(allStr,2)))
    print("hex "+str(hex(int(allStr,2))))
        