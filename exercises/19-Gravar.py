arquivo = open('HelloWorld.txt', 'w')

arquivo.write('Hello \n')
arquivo.write('World')
arquivo.close()

# Leitura do Arquivo de Texto

leitura=open('HelloWorld.txt', 'r')
print(leitura.read())
leitura.close()