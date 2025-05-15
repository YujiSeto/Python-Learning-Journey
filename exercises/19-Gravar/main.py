arquivo = open('exercises/19-Gravar/HelloWorld.txt', 'w')

arquivo.write('Hello \n')
arquivo.write('World')
arquivo.close()

# Leitura do Arquivo de Texto

leitura=open('exercises/19-Gravar/HelloWorld.txt', 'r')
print(leitura.read())
leitura.close()