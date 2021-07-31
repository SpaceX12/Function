a = open('F1.txt')

c = open('F2.txt')

def swapFileData():
    with open(a, 'r') as a:
        data1 = a.read()
    
    with open(c, 'r') as a:
        data2 = c.read()

    with open(a, 'w') as a:
        a.write(data2)

    with open(c, 'w') as a:
        c.write(data1)

swapFileData()
