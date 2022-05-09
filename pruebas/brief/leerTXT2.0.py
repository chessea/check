f = open("pdi.txt", "r")
#lineas = f.readlines()
f.close()

f = open("pdi.txt", "r")
while(True):
    linea = f.readline()
    #print(linea)
    if not linea:
        break
f.close()


f = open("pdi.txt", "r")
for linea in f:
    lista=linea.split("\t")
    print(lista)
f.close()