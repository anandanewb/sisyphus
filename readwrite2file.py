def writeToFile(f,text):
    with open(f, 'w') as fo:
        fo.write(text)

def appendToFile(f,text):
    with open(f, 'a') as fo:
        fo.write(text)

def readFromFile(f):
    with open(f, 'r') as fo:
        return fo.read()
    
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'and Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nand Goodbye!\n'