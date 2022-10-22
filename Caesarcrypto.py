listascii = []
listasciie = []
def crypt(text, code):
    for i in text:
        listascii.append(int(ord(i)+code))
def tostring():
    h = ""
    for i in listascii:
        h +=chr(i)
    return h
def decrypt(text, code):
    for i in text:
        listasciie.append(int(ord(i)-code))
def tostringe():
    h = ""
    for i in listasciie:
        h +=chr(i)
    return h
while(True):
    listascii.clear()
    listasciie.clear()
    text1 = input("Text to crypt/encrypt: ")
    code1 = int(input("Code for the text: "))
    action = int(input("1 for crypt 2 for encrypt: "))
    if (action ==1):
        crypt(text1, code1)
        print(tostring())
    elif (action ==2):
        decrypt(text1, code1)
        print(tostringe())














