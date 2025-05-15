class Pessoa:
    """Isto é uma classe nova chamada Pessoa"""
    
    idade = 27

    def saudacao(self):
        print('Olá Pessoas!')

# Cria um novo objeto da classe Pessoa
rodrigo = Pessoa()

# Output: 15
print(rodrigo.idade)

# Output: <bound method Pessoa.saudacao of <__main__.Pessoa object at 0x...>>
print(rodrigo.saudacao)

# Chamando o método saudacao()
# Output: Olá Pessoas!
rodrigo.saudacao()
