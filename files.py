with open('paint.py') as f:
    read_data = f.read()
    print('Todo el archivo de un jalón')
    print(read_data)

with open('paint.py') as f:
    read_data = f.readlines()

for linea in read_data:
    print(linea)

f = open('my_file.txt', 'w')
f.write('hola\n')
f.write('bye')
f.close()
